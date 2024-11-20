from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView
from api.models import Book
from rest_framework import viewsets
# Create your views here.

class BookList(ListAPIView):
    quryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    querysets = Book.objects.all()
    serializer_class = BookSerializer
