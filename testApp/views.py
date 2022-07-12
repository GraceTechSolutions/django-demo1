from django.shortcuts import render
from .models import ToDo

# Create your views here.
def index(request):
    data = {
        'title': 'My Index Page Example'
    }
    
    return render(request, 'index.html', data)


def about(request):
    return render(request, 'about.html')

def todo(request):
    todos = ToDo.objects.all()
    data = {
        'todos': todos
    }
    return render(request, 'todo.html', data)