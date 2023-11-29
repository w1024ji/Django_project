# forecast/admin.py
from django.contrib import admin
from .models import Poll, Choice, Weather

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Weather)