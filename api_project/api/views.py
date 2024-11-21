from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView
from api.models import Book
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class BookList(ListAPIView):
    quryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    querysets = Book.objects.all()
    serializer_class = BookSerializer



class PostListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
