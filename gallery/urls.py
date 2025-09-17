# gallery/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_home, name='gallery_home'), # Changed views.home to views.gallery_home
]