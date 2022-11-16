from django_filters import rest_framework as filters
from .models import Character
class CharacterFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Character
        fields = ['name']