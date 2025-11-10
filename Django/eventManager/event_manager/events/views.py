# events/views.py
from events.models import Event
from django.shortcuts import render


def index(request):
    context = {"company": "Trybe", "events": Event.objects.all()}
    return render(request, "home.html", context)
