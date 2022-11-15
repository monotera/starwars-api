from rest_framework import serializers
from .models import Movie
from planets.serializer import PlanetSerializer

class MovieSerializer(serializers.ModelSerializer):
    planets = PlanetSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['name', 'opening_text', 'producer', 'director','planets']
