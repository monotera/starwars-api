from rest_framework import viewsets
from rest_framework.response import Response

from movies.serializer import MovieSerializer
from planets.models import Planet
from .models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        planets_ids = request.data.pop('planets_ids', [])
        movie_validator = MovieSerializer(data=request.data)
        if movie_validator.is_valid():
            new_movie = Movie(**request.data)
            new_movie.save()
            for planet_id in planets_ids:
                try:
                    planet_obj = Planet.objects.get(id=planet_id)
                    new_movie.planets.add(planet_obj)
                except Planet.DoesNotExist:
                    print("There was an error with the id.")
            movie_serialize = MovieSerializer(new_movie)
            return Response(movie_serialize.data, 201)
        return Response({"errors": movie_validator.errors}, 500)
