# models.py
from django.db import models
from django.contrib.auth.models import User


class WebcamStream(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stream_key = models.CharField(max_length=50, unique=True)
    is_live = models.BooleanField(default=False)
