from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

class Home_post(models.Model):
    title=models.CharField(max_length=100)



