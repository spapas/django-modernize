from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, UpdateView, CreateView
import core.models


class HomeTemplateView(TemplateView):
    template_name="home.html"


class PersonListView(ListView):
    model = core.models.Person


class PersonCreateView(CreateView):
    model = core.models.Person
    fields = ('first_name', 'last_name', 'sex', )
