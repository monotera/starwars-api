from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from movies.models import Movie
# Create your models here.

class Character(models.Model):
    #id = models.UUIDField()
    name = models.CharField(max_length=250),
    height = models.DecimalField(decimal_places=1, max_digits=5)
    mass = models.DecimalField(decimal_places=1, max_digits=5)
    hair_color = models.CharField(max_length=150)
    skin_color = models.CharField(max_length=150)
    eye_color = models.CharField(max_length=150)
    gender = models.CharField(max_length=7)
    movies = models.ManyToManyField(Movie, related_name='movies')
    #films

    def __str__(self) -> str:
        return f'Character: name = {self.name}, height = {str(self.height)}, mass = {str(self.mass)}, hair_color = {self.hair_color}, ' \
               f'skin_color = {self.skin_color}, eye_color = {self.eye_color}, gender = {self.gender}'