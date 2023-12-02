from django.urls import path
import user.views
from .views import MyPostsListView

urlpatterns = [
    path('login/', user.views.login, name='login'),
    path('signup/', user.views.signup, name='signup'),
    # path('logout/', user.views.logout, name='logout'),
    path('logout/', user.views.logout, name='logout'),
    path('mypage/', user.views.mypage, name='mypage'),
    path('my_posts/', MyPostsListView.as_view(), name='my_posts'),
]