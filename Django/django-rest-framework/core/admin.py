from django.contrib import admin

from formularios.playlists.models import Music, Playlist, Singer

# Register your models here.
admin.site.register(Singer)
admin.site.register(Music)
admin.site.register(Playlist)