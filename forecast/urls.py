# forecast/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_and_save_weather, name='fetch_and_save_weather'),
    path('vote/', views.vote, name='vote'),
    path('tab/', views.tab, name='tab'),
]

