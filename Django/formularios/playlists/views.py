# playlists/views.py

from django.shortcuts import render
from playlists.forms import CreateMusicForm


def music(request):
    form = CreateMusicForm()
    context = {"form": form}
    return render(request, "music.html", context)
