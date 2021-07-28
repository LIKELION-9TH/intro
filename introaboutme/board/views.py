from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Music
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import MusicBoardSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all().order_by('-id')
    serializer_class = MusicBoardSerializer
