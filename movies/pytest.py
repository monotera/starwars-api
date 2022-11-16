import json

import pytest
from django.core.management import call_command
from rest_framework.test import APIClient
from planets.models import Planet
from .models import Movie

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def data_no_planets():
    return  {
        "name": "An old Hope",
        "opening_text": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon.",
        "producer": "Gary Kurtz, Rick McCallum",
        "director": "George Lucas",
    }

@pytest.fixture
def data_with_planets():
    return  {
        "name": "An old Hope",
        "opening_text": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon.",
        "producer": "Gary Kurtz, Rick McCallum",
        "director": "George Lucas",
        "planets_ids": [12]
    }


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'planets.json')
        call_command('loaddata', 'movies.json')


class TestPlanetViewSet:
    endpoint = '/movies/'

    @pytest.mark.django_db
    def test_list(self, client):
        response = client.get(self.endpoint)
        result = json.loads(response.content)
        assert response.status_code == 200 and len(result) == 2


    @pytest.mark.django_db
    def test_create_correct_code_response(self, client, data_no_planets):
        response = client.post(self.endpoint, data_no_planets, format='json')
        assert response.status_code == 201


    @pytest.mark.django_db
    def test_create_correct_insertion(self, client, data_no_planets, django_db_setup):
        response = client.post(self.endpoint, data_no_planets, format='json')
        movies = Movie.objects.all()
        assert len(movies) == 3

    @pytest.mark.django_db
    def test_create_internal_server_error_code_response(self, client):
        response = client.post(self.endpoint, {}, format='json')
        assert response.status_code == 500

    @pytest.mark.django_db
    def test_create_response(self, client, data_no_planets, django_db_setup):
        response = client.post(self.endpoint, data_no_planets, format='json')
        result = json.loads(response.content)
        assert result['name'] == "An old Hope"

    @pytest.mark.django_db
    def test_create_relation_response(self, client, data_with_planets, django_db_setup):
        response = client.post(self.endpoint, data_with_planets, format='json')
        result = json.loads(response.content)
        assert result.get('planets',[])
