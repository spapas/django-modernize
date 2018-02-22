from django.core.management.base import BaseCommand, CommandError
from core.models import Person
import requests, json

class Command(BaseCommand):
    help = 'Read persons'

    def handle(self, *args, **options):
        r = requests.get('https://randomuser.me/api/?results=50')
        j = json.loads(r.content)

        persons = [
            Person(
                first_name=p['name']['first'],
                last_name=p['name']['last'],
                sex=p['gender'][0].upper(),
            ) for p in j['results']
        ]

        Person.objects.bulk_create(persons)

