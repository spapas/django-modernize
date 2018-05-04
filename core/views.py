from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic import ListView, UpdateView, CreateView, DetailView
import core.models
import core.filters


class HomeTemplateView(TemplateView):
    template_name="home.html"


class PersonListView(ListView):
    model = core.models.Person
    paginate_by = 9

    def get_queryset(self):
        self.filter = core.filters.PersonFilter(self.request.GET, queryset=super().get_queryset())
        return self.filter.qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['filter'] = self.filter
        return ctx



class PersonDetailView(DetailView):
    model = core.models.Person

    def get_template_names(self):
        if self.request.is_ajax():
            return 'core/person_partial/person_modal.html'

        return super().get_template_names()


class PersonModernListView(ListView):
    model = core.models.Person
    paginate_by = 9
    template_name="core/modern_person_list.html"

    def get_queryset(self):
        self.filter = core.filters.PersonFilter(self.request.GET, queryset=super().get_queryset())
        return self.filter.qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['filter'] = self.filter
        return ctx

    def get_template_names(self):
        if self.request.is_ajax():
            if self.request.GET.get('page'):
                return 'core/person_partial/person_page.html'
            return 'core/person_partial/person_filter_page.html'

        return super().get_template_names()


class PersonCreateView(CreateView):
    model = core.models.Person
    fields = ('first_name', 'last_name', 'sex', 'dob', 'nat', 'address', 'phone', 'cell' ,'large_photo', 'medium_photo', 'small_photo',  )

    def get_template_names(self):
        if self.request.is_ajax():
            return 'core/person_partial/modal_person_form.html'

        return super().get_template_names()

    def get_success_url(self):
        if self.request.is_ajax():
            return reverse('person_form_success')

        return super().get_success_url()



class PersonSuccessTemplateView(TemplateView):
    template_name = 'core/person_partial/person_form_success.html'

    def dispatch(self, *args, **kwargs):
        response = super(PersonSuccessTemplateView, self).dispatch(*args, **kwargs)
        response['X-IC-Trigger'] = 'refreshList'
        return response


class PersonUpdateView(UpdateView):
    model = core.models.Person
    fields = ('first_name', 'last_name', 'sex', 'dob', 'nat', 'address', 'phone', 'cell' ,'large_photo', 'medium_photo', 'small_photo',  )

    def get_template_names(self):
        if self.request.is_ajax():
            return 'core/person_partial/modal_person_form.html'

        return super().get_template_names()

    def get_success_url(self):
        if self.request.is_ajax():
            return reverse('person_form_success')

        return super().get_success_url()

    def dispatch(self, *args, **kwargs):
        response = super(PersonUpdateView, self).dispatch(*args, **kwargs)
        if response.status_code == 200:
            # Do nothing
            pass
        else:
            response['X-IC-Trigger'] = 'refreshList'
        return response

