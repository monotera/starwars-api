from django.test import TestCase

from .models import Movie
from .models import Planet
from .serializer import MovieSerializer


# Create your tests here.

class PlanetsModelTests(TestCase):
    fixtures = ['movies.json', 'planets.json']
    data = {
        "name": "A New Hope",
        "opening_text": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon.",
        "producer": "Gary Kurtz, Rick McCallum",
        "director": "George Lucas",
    }

    def test_movie_creation_obj_from_dict(self):
        new_movie = Movie(**self.data)
        self.assertEqual(new_movie.name, self.data["name"])

    def test_fetch_all_movies(self):
        movies = Movie.objects.all()
        self.assertEqual(len(movies), 2)

    def test_object_creation(self):
        new_movie = Movie(**self.data)
        new_movie.save()
        movies = Movie.objects.all()
        self.assertEqual(len(movies), 3)

    def test_relation_creation(self):
        new_movie = Movie(**self.data)
        new_movie.save()
        planet = Planet.objects.get(id=11)
        new_movie.planets.add(planet)
        self.assertTrue(new_movie.planets.all())

    def test_serialize_planet(self):
        serialize_planet = MovieSerializer(data=self.data)
        self.assertTrue(serialize_planet.is_valid())
