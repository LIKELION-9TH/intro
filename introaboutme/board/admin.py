from django.contrib import admin
from .models import Music


class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Music, MusicAdmin)
