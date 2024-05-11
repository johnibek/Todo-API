from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        user = super(CustomUser, self)
        user.set_password(self.password)
        user.save()
        return user

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name


class Todo(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    body = models.CharField(max_length=250)
    datetime = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"Todo of {self.user.username}"



