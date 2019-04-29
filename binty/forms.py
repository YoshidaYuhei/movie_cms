import csv
import io

from django import forms
from django.contrib.auth import get_user_model
from dal import autocomplete
from .models import Content, Cast, Director, Genre


class CustomUserForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'icon']


class ContentForm(forms.ModelForm):

    class Meta:
        model = Content
        fields = ['title', 'thumbnail', 'duration', 'country', 'release_date', 'genre', 'director', 'cast', 'awards']
        widgets = {
            'cast': autocomplete.ModelSelect2Multiple(url='binty:cast-autocomplete'),
            'genre': autocomplete.ModelSelect2(url='binty:genre-autocomplete'),
            'director': autocomplete.ModelSelect2(url='binty:director-autocomplete')
        }


class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = ['name', 'history']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name', 'history']


class UploadFileForm(forms.Form):
    file = forms.ImageField()


class TestForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    foreign = forms.ModelChoiceField(queryset=Director.objects.all())
    manytomany = forms.ModelMultipleChoiceField(queryset=Cast.objects.all())


class DbImportForm(forms.Form):
    start = forms.IntegerField(min_value=1)
    end = forms.IntegerField()


class CSVUploadForm(forms.Form):
    file = forms.FileField(label='CSVファイル', help_text='CSVをアップロードしてください')

    def save(self):
        Content.objects.bulk_create(self._instances, ignore_conflicts=True)
        Content.objects.bulk_update(self._instances, fields=['title'])
