from rest_framework import serializers
from movies.models import Movie
from .models import Character
from movies.serializer import MovieSerializer


class CharacterSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = ['id','name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'gender', 'movies']