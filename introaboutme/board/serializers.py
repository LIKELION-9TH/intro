# 필드 설정
from django import forms
from rest_framework import serializers
from .models import Music, Location, Hobby, Me


class MusicBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('title', 'description', 'banner_image')


class LocationBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('title', 'description', 'banner_image')


class HobbyBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby
        fields = ('title', 'banner_image')


class MeBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Me
        fields = ('title', 'description', 'banner_image')
