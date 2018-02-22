import core.views
from django.urls import path

urlpatterns = [
    path('', core.views.HomeTemplateView.as_view(), name='home', ),
    path('person_list', core.views.PersonListView.as_view(), name='person_list', ),
    path('person_create', core.views.PersonCreateView.as_view(), name='person_create', ),
]
