# gallery/admin.py
from django.contrib import admin
from .models import Album, Photo, Comment, Like

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Like)