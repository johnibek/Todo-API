from django.contrib import admin
from .models import Todo, CustomUser


admin.site.register(Todo)
admin.site.register(CustomUser)