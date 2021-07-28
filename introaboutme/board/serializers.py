# 필드 설정
from django import forms
from rest_framework import serializers
from .models import Music


class MusicBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('title', 'description', 'banner_image')
