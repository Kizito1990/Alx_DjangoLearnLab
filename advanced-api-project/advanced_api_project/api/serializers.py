from rest_framework import serializers
from.models import Author, Book
from django.utils import timezone





class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source = 'author.name', read_only=True)
#Serializes the Book model. Includes custom validation to ensure the
   # publication year is not in the future.
    class Meta:
        model = Book
        fields =['id', 'title', 'author', 'author_name', 'publication_year']


    def validate_published_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("The published date cannot be in the future.")
            return value



class AuthorSerializer(serializers.ModelSerializer):
    # Serializes the Author model. Includes a nested serializer to serialize
   # related books dynamically
    books = BookSerializer()
    class Meta:
        model = Author
        fields = ['id', 'name']
