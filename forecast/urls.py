# forecast/urls.py

from django.urls import path
from .views import fetch_and_save_weather

urlpatterns = [ # namespace 추가함
    path('fetch-weather/', fetch_and_save_weather, name='fetch_weather'),
]
