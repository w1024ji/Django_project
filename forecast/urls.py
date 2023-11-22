# forecast/urls.py

from django.urls import path
from .views import fetch_and_save_weather
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ # namespace 추가함
    path('', fetch_and_save_weather, name='landing_page'), 
    path('fetch-weather/', fetch_and_save_weather, name='fetch_weather'),
]
