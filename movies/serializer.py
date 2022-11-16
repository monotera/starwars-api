from rest_framework import serializers
from .models import Movie
from planets.serializer import PlanetSerializer
from planets.models import Planet
class MovieSerializer(serializers.ModelSerializer):
    planets = PlanetSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['id','name', 'opening_text', 'producer', 'director','planets']

