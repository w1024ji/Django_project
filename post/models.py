from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Weather(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='weather/images/', blank=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/post/weather/{self.slug}'

class Post(models.Model):
    title = models.CharField(max_length=30, validators=[MinLengthValidator(1)])
    weather = models.ForeignKey(Weather, null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField(max_length=60, validators=[MinLengthValidator(1)])
    
    head_image = models.ImageField(upload_to='post/images/%Y/%m/%d/', blank=True)
    
    created_at = models.DateField(default=timezone.now)
    
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'
    
    def get_absolute_url(self):
        return f'/post/{self.pk}/'