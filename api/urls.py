from django.urls import path
from . import views

urlpatterns = [
    path('todo-items/', views.todo_list_view, name='todo_list'),
    path('todo-items/<int:id>', views.todo_detail_view, name='todo_detail'),
]