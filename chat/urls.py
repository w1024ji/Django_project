from django.urls import path
from .views import Index, Room

from . import views


urlpatterns = [
#    path("", views.index, name="index"),
#    path("<str:room_name>/", views.room, name="room"),
    path('', Index.as_view(), name='index'),
    path('<str:room_name>/', Room.as_view(), name='room'),
]