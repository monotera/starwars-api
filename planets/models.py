from django.db import models

# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=250)
    rotation_period = models.IntegerField()
    orbital_period = models.IntegerField()
    diameter = models.IntegerField()
    climate = models.CharField(max_length=250)
    gravity = models.CharField(max_length=250)
    terrain = models.CharField(max_length=250)
    surface_water = models.IntegerField()
    population = models.IntegerField()

    def __str__(self) -> str:
        return f'Planet: name = {self.name}, rotation_period = {str(self.rotation_period)}, orbital_period = {str(self.orbital_period)}, ' \
               f'diameter = {str(self.diameter)}, climate = {self.climate}, gravity = {self.gravity}, terrain = {self.terrain}, ' \
               f'surface_water = {str(self.surface_water)}, population = {self.population}'