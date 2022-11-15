from django.db import models


# Create your models here.
class Movie(models.Model):
    # id = models.UUIDField()
    # movie_planets
    name = models.CharField(max_length=250)
    opening_text = models.CharField(max_length=350)
    producer = models.CharField(max_length=150)
    director = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f'Movie: name = {self.name}, opening_text = {self.opening_text}, producer = {self.producer},' \
               f' director = {self.director}'
