import datetime
import random

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView

from .models import Event


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def random_404(request):
    try:
        1 / random.choice([0, 1])
        return HttpResponse('<h1>Hello</h1>')
    except Exception as err:
        return HttpResponseNotFound(f'<h1>It\'s Failed :(</h1><p>error: {err}</p>')


def list_events(request):
    e = Event.objects.all()
    return render(request, 'events/event_list.html', {'event_list': e})


class ListEventsView(ListView):
    model = Event
