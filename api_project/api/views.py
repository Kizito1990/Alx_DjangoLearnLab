from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics.ListAPIView

# Create your views here.

class BookList(serializers.ListAPIView):
    quryset = Book.objects.all()
    serializer_class = BookSerializer
