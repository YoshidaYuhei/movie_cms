from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import SignUpForm


class SignUpView(FormView):
    from_class = SignUpForm
    template_name = 'registration/signup.html'


class SignUpDoneView(TemplateView):
    pass
