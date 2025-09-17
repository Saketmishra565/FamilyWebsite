# family_calendar/views.py
from django.shortcuts import render
from .models import Event

def home(request):
    events = Event.objects.all().order_by('start_time')
    return render(request, 'calendarr/home.html', {'events': events})