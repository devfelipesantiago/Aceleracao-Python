# events/views.py
from django.http import Http404
from events.models import Event
from django.shortcuts import get_object_or_404, render


def index(request):
    context = {"company": "Trybe", "events": Event.objects.all()}
    return render(request, "home.html", context)


# Na função event_details, o parâmetro event_id será recebido e utilizado para
# resgatar o evento específico que se quer renderizar. Esse resgate é feito com
# o uso da função get_object_or_404(), essa função recebe dois parâmetros: o
# primeiro é o modelo a ser resgatado e o segundo indica a busca a ser feita.
# No exemplo acima, é buscado por um Event cujo id é igual ao event_id
# recebido como parâmetro. Caso o evento não seja encontrado, será levantada uma exceção do tipo Http404.
def event_details(request, event_id):
    try:
        event = get_object_or_404(Event, id=event_id)
        return render(request, "details.html", {"event": event})
    except Http404:
        return render(request, "404.html")
