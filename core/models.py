from django.db import models
from django.urls import reverse


SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Person(models.Model):
    first_name = models.CharField(max_length=128, )
    last_name = models.CharField(max_length=128, )
    email = models.EmailField()
    dob = models.DateField()
    sex = models.CharField(max_length=4, choices=SEX_CHOICES, )
    nat = models.CharField(max_length=4, )
    address = models.CharField(max_length=128, )
    phone = models.CharField(max_length=128, )
    cell = models.CharField(max_length=128, )
    large_photo = models.URLField()
    medium_photo = models.URLField()
    small_photo = models.URLField()

    def get_absolute_url(self):
        return reverse('person_view', args=[str(self.id)])
