# playlists/views.py

from django.shortcuts import redirect, render
from formularios.playlists.models import Music, Singer
from playlists.forms import CreateMusicForm, CreateSingerForm


def music(request):
    form = CreateMusicForm()

    if request.method == "POST":
        form = CreateMusicForm(request.POST)
    if form.is_valid():
        Music.objects.create(**form.cleaned_data)
        return redirect("home-page")

    context = {"form": form}
    return render(request, "music.html", context)


def index(request):
    context = {"music": Music.objects.all()}
    return render(request, "home.html", context)


def singer(request):
    form = CreateSingerForm()

    if request.method == "POST":
        form = CreateSingerForm(request.POST)

        if form.is_valid():
            Singer.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "singer.html", context)
