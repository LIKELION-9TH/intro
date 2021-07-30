from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Hobby, Location, Me, Music
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import HobbyBoardSerializer, LocationBoardSerializer, MeBoardSerializer, MusicBoardSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all().order_by('-id')
    serializer_class = MusicBoardSerializer



class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('-id')
    serializer_class = LocationBoardSerializer



class HobbyViewSet(viewsets.ModelViewSet):
    queryset = Hobby.objects.all().order_by('-id')
    serializer_class = HobbyBoardSerializer



class MeViewSet(viewsets.ModelViewSet):
    queryset = Me.objects.all().order_by('-id')
    serializer_class = MeBoardSerializer
