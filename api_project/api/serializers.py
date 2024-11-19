from .models import Book
from rest_framework import serializer


class BookSerializer(serializer.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'



