from django.contrib import admin
from .models import Hobby, Location, Me, Music


class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class HobbyAdmin(admin.ModelAdmin):
    list_display = ('title', )

class MeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Music, MusicAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Hobby, HobbyAdmin)
admin.site.register(Me, MeAdmin)
