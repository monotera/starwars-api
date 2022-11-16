import json

import pytest
from django.core.management import call_command
from rest_framework.test import APIClient

from .models import Character


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def data_no_movies():
    return {
        "name": "Test Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "brown",
        "skin_color": "fair",
        "eye_color": "blue",
        "gender": "male",
    }


@pytest.fixture
def data_with_movies():
    return {
        "name": "Test Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "brown",
        "skin_color": "fair",
        "eye_color": "blue",
        "gender": "male",
        "movies_ids": [4]
    }


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'planets.json')
        call_command('loaddata', 'movies.json')
        call_command('loaddata', 'characters.json')


class TestPlanetViewSet:
    endpoint = '/characters/'
    character_name = "Anakin TestWalker"
    @pytest.mark.django_db
    def test_list(self, client):
        response = client.get(self.endpoint)
        result = json.loads(response.content)
        assert response.status_code == 200 and len(result) == 2

    @pytest.mark.django_db
    def test_find_character_by_name(self, client, django_db_setup):
        response = client.get(self.endpoint,{'name': self.character_name})
        result = json.loads(response.content)
        assert result[0]['name'] == self.character_name
    @pytest.mark.django_db
    def test_create_correct_code_response(self, client, data_no_movies):
        response = client.post(self.endpoint, data_no_movies, format='json')
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_correct_insertion(self, client, data_no_movies, django_db_setup):
        response = client.post(self.endpoint, data_no_movies, format='json')
        characters = Character.objects.all()
        assert len(characters) == 3

    @pytest.mark.django_db
    def test_create_internal_server_error_code_response(self, client):
        response = client.post(self.endpoint, {}, format='json')
        assert response.status_code == 500

    @pytest.mark.django_db
    def test_create_response(self, client, data_no_movies, django_db_setup):
        response = client.post(self.endpoint, data_no_movies, format='json')
        result = json.loads(response.content)
        assert result['name'] == "Test Skywalker"

    @pytest.mark.django_db
    def test_create_relation_response(self, client, data_with_movies, django_db_setup):
        response = client.post(self.endpoint, data_with_movies, format='json')
        result = json.loads(response.content)
        assert result.get('movies', [])


