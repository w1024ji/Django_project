from django.contrib import admin
from .models import Post, Weather

# Register your models here.
admin.site.register(Post)
admin.site.register(Weather)