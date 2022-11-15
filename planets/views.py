from .serializer import PlanetSerializer
from rest_framework import viewsets
from .models import Planet


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer