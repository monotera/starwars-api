from django.db import models
from planets.models import Planet

# Create your models here.
class Movie(models.Model):
    # id = models.UUIDField()
    # movie_planets
    name = models.CharField(max_length=250)
    opening_text = models.CharField(max_length=350)
    producer = models.CharField(max_length=150)
    director = models.CharField(max_length=250)
    planets = models.ManyToManyField(Planet, related_name="movie_planet", blank=True)
    def __str__(self) -> str:
        return f'Movie: name = {self.name},\n opening_text = {self.opening_text}\n, producer = {self.producer}\n,' \
               f' director = {self.director}\n'
