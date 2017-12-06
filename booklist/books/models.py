from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    date_published = models.DateField(auto_now_add=True)
    number_pages = models.IntegerField()
    type_book = models.CharField(max_length=250)

class Meta:
    ordering =('-date_published',)
def __str__(self):
    return self.title
    
