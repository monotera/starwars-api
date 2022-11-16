from django.test import TestCase

from .models import Planet
from .serializer import PlanetSerializer


# Create your tests here.

class PlanetsModelTests(TestCase):
    fixtures = ['planets.json']
    data = {
        "name": "Ord Mantell",
        "rotation_period": "26",
        "orbital_period": "334",
        "diameter": "14050",
        "climate": "temperate",
        "gravity": "1 standard",
        "terrain": "plains, seas, mesas",
        "surface_water": 10,
        "population": "4000000000"
    }

    def test_planet_creation_obj_from_dict(self):
        """
        Tests if the object was created sucessfully from a dictionary
        """
        new_planet = Planet(**self.data)
        self.assertEqual(new_planet.name, self.data["name"])

    def test_fetch_all_planets(self):
        planets = Planet.objects.all()
        self.assertEqual(len(planets), 3)

    def test_object_creation(self):
        new_planet = Planet(**self.data)
        new_planet.save()
        planets = Planet.objects.all()
        self.assertEqual(len(planets), 4)

    def test_fetch_planet(self):
        planet = Planet.objects.filter(name="Ord Mantest").first()
        self.assertEqual(planet.id, 13)

    def test_serialize_planet(self):
        serialize_planet = PlanetSerializer(data=self.data)
        self.assertTrue(serialize_planet.is_valid())
