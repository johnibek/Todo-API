from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='category')

urlpatterns = [
    path('todo-items/', views.TodoListAPIView.as_view(), name='todo_list'),
    path('todo-items/<int:id>', views.TodoDetailAPIView.as_view(), name='todo_detail'),
]

urlpatterns += router.urls