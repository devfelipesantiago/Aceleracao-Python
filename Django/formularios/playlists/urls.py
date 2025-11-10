# playlists/urls.py

from django.urls import path
from playlists.views import music


urlpatterns = [
    path("musics/", music, name="musics-page"),
]
