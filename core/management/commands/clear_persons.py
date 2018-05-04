from django.core.management.base import BaseCommand, CommandError
from core.models import Person
import requests, json, datetime

class Command(BaseCommand):
    help = 'Clear persons'

    def handle(self, *args, **options):
        Person.objects.all().delete()

