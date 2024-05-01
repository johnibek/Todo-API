from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

class Todo(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE, blank=True, null=True)
    body = models.CharField(max_length=250)
    datetime = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"Todo of {self.user.username}"
