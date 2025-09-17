# calendarr/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='calendar_home'), # Add name='calendar_home' here
]