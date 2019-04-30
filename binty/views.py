import csv
import logging
from io import TextIOWrapper
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth import views as auth_view
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from dal import autocomplete
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Content, Cast, Genre, Director
from .forms import ContentForm, CastForm, CSVUploadForm, GenreForm, DirectorForm, DbImportForm, CustomUserForm
from .webscraping import WebScraping


User = get_user_model()


class IndexView(generic.ListView):
    model = Content
    template_name = 'binty/index.html'
    context_object_name = 'page_obj'
    genre_list = Genre.objects.all()

    def __init__(self):
        formatter = '%(levelname)s : %(asctime)s : %(message)s'
        logging.basicConfig(level=logging.DEBUG, format=formatter)

    def get_queryset(self):
        return Content.objects.order_by('-id')

    def get(self, request):
        lists = self.get_queryset()
        page_obj = pagenate_query(request, lists, settings.PAGE_PER_ITEM)
        context = {
            'page_obj': page_obj,
            'genre_list': self.genre_list,
        }
        return render(request, self.template_name, context)

    def post(self, request):

        if 'search_word' in request.POST:
            word = request.POST['search_word']
            lists = Content.objects.filter(title__contains=word)
            page_obj = pagenate_query(request, lists, settings.PAGE_PER_ITEM)
            context = {
                'page_obj': page_obj,
                'genre_list': self.genre_list,
            }
            return render(request, self.template_name, context)

        if 'genre_select' in request.POST:
            genre_id = request.POST['genre_select']
            genre_obj = Genre.objects.get(id=genre_id)
            lists = Content.objects.filter(genre=genre_obj)
            page_obj = pagenate_query(request, lists, settings.PAGE_PER_ITEM)
            context = {
                'page_obj': page_obj,
                'genre_list': self.genre_list,
            }
            return render(request, self.template_name, context)

        if 'good' in request.POST:
            content_id = request.POST['good']
            content = Content.objects.get(pk=content_id)
            login_user_id = request.user.id
            user = User.objects.get(pk=login_user_id)
            content.goods.add(user)
            content.save()
            return self.get(request)


class DetailView(generic.DetailView):
    model = Content
    template_name = 'binty/detail.html'

    def get(self, request, content_id):
        lists = Content.objects.get(pk=content_id)
        context = {
            'movie': lists,
            'foo': lists.thumbnail
        }
        return render(request, self.template_name, context)


class CastListView(generic.ListView):
    template_name = 'binty/castlist.html'

    def get(self, request, cast_id):
        actor = Cast.objects.get(pk=cast_id)
        contents = Content.objects.filter(cast=actor)
        context = {
            'actor': actor,
            'contents': contents
        }
        return render(request, self.template_name, context)


class RegisterView(generic.CreateView):
    template_name = 'binty/forms.html'
    model = Content
    form_class = ContentForm()

    def get(self, request):
        context = {
            'form': self.form_class,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        url = reverse('binty:register')
        if 'content_form' in request.POST:
            form = ContentForm(request.POST, request.FILES)
            if form.is_valid():
                # manytomanyのデータは取り出して持っておく
                casts = form.cleaned_data['cast']
                # manytomanyのデータは直接文字列を入れられないので辞書から除外する
                del form.cleaned_data['cast']
                # manytomanyフィールド以外を設定したインスタンスを生成
                cont = Content.objects.create(**form.cleaned_data)

                # manytomanyデータの入れ方
                for cast in casts:
                    cont.cast.add(cast)

                cont.save()

                return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect(url)


def sub_form_view(request):
    if request.method == 'GET' and 'btn' in request.GET:
        template = loader.get_template('binty/subform.html')
        print(request.GET)
        btn = request.GET.get('btn')
        if btn == 'genre':
            form = GenreForm()
        elif btn == 'director':
            form = DirectorForm()
        elif btn == 'cast':
            form = CastForm()

        context = {
            'form': form,
        }
        return render(request, template, context)


def pagenate_query(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


class CastAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Cast.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class GenreAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Genre.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class DirectorAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Director.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class ContentImport(generic.FormView):
    template_name = 'binty/import.html'
    success_url = reverse_lazy('binty:index')
    form_class = CSVUploadForm
    scrape = WebScraping()

    def get(self, request):
        form = self.form_class(request.GET)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if 'file' in request.FILES:

            csvfile = TextIOWrapper(request.FILES['file'].file)
            self.scrape.csv_import(csvfile)

        if 'db_import' in request.POST:
            form = DbImportForm(request.POST)
            if form.is_valid():
                start = form.cleaned_data['start']
                end = form.cleaned_data['end']

                self.scrape.scrape(start, end)

        return HttpResponseRedirect(reverse('binty:index'))


class MyPageView(generic.DetailView):
    model = User
    template_name = 'registration/mypage.html'

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        contents = Content.objects.filter(goods=user)
        context = {
            'contents': contents
        }
        return render(request, self.template_name, context)


class LogoutView(auth_view.LogoutView):
    template_name = 'registration/logout.html'


class LoginView(auth_view.LoginView):
    template_name = 'registration/login.html'
    model = User

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request, self.template_name)


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = CustomUserForm

    def __init__(self):
        formatter = '%(levelname)s : %(asctime)s : %(message)s'
        logging.basicConfig(level=logging.DEBUG, format=formatter)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        logging.debug(request.POST)
        form = self.form_class(data=request.POST)
        logging.debug(form.errors)
        logging.debug(form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('binty:index'))

        return HttpResponseRedirect(reverse('binty:index'))


