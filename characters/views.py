from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.response import Response

from characters.serializer import CharacterSerializer
from movies.models import Movie
from .character_filter import CharacterFilter
from .models import Character


# Create your views here.

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CharacterFilter

    def create(self, request, *args, **kwargs):
        movies_ids = request.data.pop('movies_ids', [])
        character_validator = CharacterSerializer(data=request.data)
        if character_validator.is_valid():
            new_character = Character(**request.data)
            new_character.save()
            for movie_id in movies_ids:
                try:
                    movie_obj = Movie.objects.get(id=movie_id)
                    new_character.movies.add(movie_obj)
                except Movie.DoesNotExist:
                    print("There was an error with the id.")
            character_serialize = CharacterSerializer(new_character)
            return Response(character_serialize.data, 201)
        return Response({"errors": character_validator.errors}, 500)
