from movies.serializer import MovieSerializer
from rest_framework import viewsets
from .models import Movie
from django_filters import rest_framework as filters

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.DjangoFilterBackend,)