from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, UpdateView, CreateView
import core.models


class HomeTemplateView(TemplateView):
    template_name="home.html"


class PersonListView(ListView):
    model = core.models.Person
    paginate_by = 9


class PersonModernListView(ListView):
    model = core.models.Person
    paginate_by = 9
    template_name="core/modern_person_list.html"

    def get_template_names(self):
        if self.request.is_ajax():
            return 'core/partial/person_page.html'

        return super().get_template_names()


class PersonCreateView(CreateView):
    model = core.models.Person
    fields = ('first_name', 'last_name', 'sex', )

    def get_template_names(self):
        if self.request.is_ajax():
            return 'core/partial/person_form.html'

        return super().get_template_names()
