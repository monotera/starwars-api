from django.test import TestCase

from movies.models import Movie
from .models import Character
from .serializer import CharacterSerializer


# Create your tests here.

class PlanetsModelTests(TestCase):
    fixtures = ['movies.json', 'characters.json', 'planets.json']
    data = {
        "name": "Anakin Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "brown",
        "skin_color": "fair",
        "eye_color": "blue",
        "gender": "male",
    }

    def test_character_creation_obj_from_dict(self):
        new_character = Character(**self.data)
        self.assertEqual(new_character.name, self.data["name"])

    def test_fetch_all_characters(self):
        characters = Character.objects.all()
        self.assertEqual(len(characters), 2)

    def test_object_creation(self):
        new_character = Character(**self.data)
        new_character.save()
        characters = Character.objects.all()
        self.assertEqual(len(characters), 3)

    def test_relation_creation(self):
        new_character = Character(**self.data)
        new_character.save()
        movie = Movie.objects.get(id=4)
        new_character.movies.add(movie)
        self.assertTrue(new_character.movies.all())

    def test_serialize_character(self):
        serialize_character = CharacterSerializer(data=self.data)
        self.assertTrue(serialize_character.is_valid())
