import django_filters
from core.models import Person

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'nat', 'sex',  ]
