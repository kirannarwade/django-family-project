from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.ImageField()
    city = models.CharField(max_length=30)

class Fmember(models.Model):
    fname = models.ForeignKey(Person, on_delete=models.CASCADE)
    fmname = models.CharField(max_length=30)
    frelation = models.CharField(max_length=30)