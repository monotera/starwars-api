import json

import pytest
from django.core.management import call_command
from rest_framework.test import APIClient
from .models import Planet

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def data():
    return {
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


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'planets.json')


class TestPlanetViewSet:
    endpoint = '/planets/'

    @pytest.mark.django_db
    def test_list(self, client):
        response = client.get(self.endpoint)
        result = json.loads(response.content)
        assert response.status_code == 200 and len(result) == 3

    @pytest.mark.django_db
    def test_create_correct_code_response(self, client, data):
        response = client.post(self.endpoint, data, format='json')
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_correct_insertion(self, client, data, django_db_setup):
        response = client.post(self.endpoint, data, format='json')
        planets = Planet.objects.all()
        assert len(planets) == 4

    @pytest.mark.django_db
    def test_create_bad_request_code_response(self, client, data):
        response = client.post(self.endpoint, {}, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_create_response(self, client, data, django_db_setup):
        response = client.post(self.endpoint, data, format='json')
        result = json.loads(response.content)
        assert result['name'] == "Ord Mantell"
