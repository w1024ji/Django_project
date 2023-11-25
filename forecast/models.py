# forecast/models.py

from django.db import models

class Weather(models.Model):
    base_date = models.CharField(max_length=8, default='20231116')
    base_time = models.CharField(max_length=4, default='0000')
    category = models.CharField(max_length=50, default='')
    fcst_date = models.CharField(max_length=8, default='20231116')
    fcst_time = models.CharField(max_length=4, default='0000')
    fcst_value = models.CharField(max_length=10, default='0')
    nx = models.IntegerField(default=0)
    ny = models.IntegerField(default=0)

    
class Poll(models.Model):
    question = models.CharField(max_length=200)

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)