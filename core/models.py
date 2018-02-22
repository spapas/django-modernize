from django.db import models
from django.urls import reverse


SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Person(models.Model):
    first_name = models.CharField(max_length=128, )
    last_name = models.CharField(max_length=128, )
    sex = models.CharField(max_length=4, choices=SEX_CHOICES, )

    def get_absolute_url(self):
        return reverse('person_view', args=[str(self.id)])
