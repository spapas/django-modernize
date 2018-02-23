from django.core.management.base import BaseCommand, CommandError
from core.models import Person
import requests, json, datetime

class Command(BaseCommand):
    help = 'Read persons'

    def handle(self, *args, **options):
    
        def get_address(p):
            street = p['location']['street'].title()
            city = p['location']['city'].title()
            state = p['location']['state'].title()
            postcode = p['location']['postcode']
            return f'{street} {city} {state} {postcode}' 
    
        r = requests.get('https://randomuser.me/api/?results=50')
        j = json.loads(r.content)

        persons = [
            Person(
                first_name=p['name']['first'].title(),
                last_name=p['name']['last'].title(),
                email=p['email'],
                address=get_address(p),
                dob=datetime.datetime.strptime(p['dob'].split(' ')[0], "%Y-%m-%d") ,
                phone=p['phone'],
                cell=p['cell'],
                nat=p['nat'],
                large_photo=p['picture']['large'],
                medium_photo=p['picture']['medium'],
                small_photo=p['picture']['thumbnail'],
                
                sex=p['gender'][0].upper(),
            ) for p in j['results']
        ]

        Person.objects.bulk_create(persons)

