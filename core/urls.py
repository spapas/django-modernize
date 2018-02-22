import core.views
from django.urls import path

urlpatterns = [
    path('', core.views.HomeTemplateView.as_view(), name='home', ),
    path('person_list', core.views.PersonListView.as_view(), name='person_list', ),
    path('person_view/<int:pk>/', core.views.PersonDetailView.as_view(), name='person_view', ),
    path('modern_person_list', core.views.PersonModernListView.as_view(), name='modern_person_list', ),
    path('person_create', core.views.PersonCreateView.as_view(), name='person_create', ),
]
