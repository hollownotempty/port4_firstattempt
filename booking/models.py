from django.db import models

# Create your models here.


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    message = models.CharField(max_length=500)
