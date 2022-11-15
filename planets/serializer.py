from rest_framework import serializers
from planets.models import Planet

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ['name','rotation_period','orbital_period','diameter','climate','gravity']
