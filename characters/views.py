from django.http import HttpResponse
from .models import Character
from.serializer import CharacterSerializer
from movies.models import Movie
from planets.models import Planet
from rest_framework import serializers
from movies.serializer import MovieSerializer
from rest_framework.request import Request
from rest_framework.renderers import JSONRenderer
# Create your views here.
def hello_world(request):
    serializer_context = {
        'request': Request(request),
    }
    ch = Character.objects.all().first()
    #print(luke.planets.al
    s = CharacterSerializer(ch,context=serializer_context)
    json = JSONRenderer().render(s.data)
    print(json)
    return HttpResponse(json, content_type="application/json")
