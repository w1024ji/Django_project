from typing import Any
from django import http
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Weather
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.core.exceptions import PermissionDenied
from django import forms


# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'weather']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            form.fields['weather'].queryset = Weather.objects.all()
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/post')
    
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'weather']
    template_name = 'post/post_update_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/post/'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
        
def weather_page(request, slug):
    if slug == 'no_category' :
        weather = '미분류'
        post_list = Post.objects.filter(weather=None)
    else:
        weather = Weather.objects.get(slug=slug)
        post_list = Post.objects.filter(weather=weather)
        
    return render (
        request,
        'post/post_list.html',
        {
            'post_list' : post_list,
            'weathers' : Weather.objects.all(),
            'no_weathers_post_count' : Post.objects.filter(weather=None).count(),
            'weather' : weather,
        }
    )

