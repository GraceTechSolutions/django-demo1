from django.urls import path
from .views import index, about, todo


urlpatterns = [
    path('', index),
    path('about', about),
    path('todo', todo)
]
