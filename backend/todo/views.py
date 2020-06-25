from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets          # added this
from .serializers import TodoSerializer      # added this
from .models import Todo                     # added this

class TodoView(viewsets.ModelViewSet):       # added this
  serializer_class = TodoSerializer          # added this
  queryset = Todo.objects.all()              # added this