from django.contrib import admin
from .models import Todo, CustomUser, Category


admin.site.register(Todo)
admin.site.register(CustomUser)
admin.site.register(Category)