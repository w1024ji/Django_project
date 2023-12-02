from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.PostCreate.as_view(), name='create'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='post'),
    path('update_post/<int:pk>', views.PostUpdate.as_view(), name='update'),
    path('delete_post/<int:pk>', views.PostDelete.as_view(), name='delete'),
    path('weather/<str:slug>/', views.weather_page),
]