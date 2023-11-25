# forecast/urls.py
from django.urls import path
from .views import fetch_and_save_weather, poll_detail, vote

urlpatterns = [
    path('', fetch_and_save_weather, name='landing_page'),
    path('fetch-weather/', fetch_and_save_weather, name='fetch_weather'),
    path('<int:poll_id>/', poll_detail, name='poll_detail'),
    path('vote/', vote, name='vote'),
]

