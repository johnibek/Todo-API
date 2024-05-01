from django.shortcuts import render
from api.models import Todo

def home(request):
    todo_items = Todo.objects.all()
    return render(request, 'home.html', {'todo_items': todo_items})