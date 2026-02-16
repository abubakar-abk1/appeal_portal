from django.db import models
from datetime import datetime

class Appeal(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000000)
    created_at = models.DateTimeField(default= datetime.now(), blank=True)
    