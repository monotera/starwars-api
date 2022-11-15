from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from characters.serializer import CharacterSerializer
from rest_framework import viewsets
from .models import Character
from rest_framework.response import Response
# Create your views here.

class CharacterViewSet(viewsets.ModelViewSet):
        queryset = Character.objects.all()
        serializer_class  = CharacterSerializer
