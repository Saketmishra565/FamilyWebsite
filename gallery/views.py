# gallery/views.py
from django.shortcuts import render
from .models import Photo, Video  # This import is correct here, not in urls.py

def gallery_home(request):
    photos = Photo.objects.all().order_by('-upload_date')
    videos = Video.objects.all().order_by('-upload_date')
    return render(request, 'gallery/gallery.html', {'photos': photos, 'videos': videos})