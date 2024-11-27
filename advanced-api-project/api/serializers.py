from rest_framework import serializers
from.models import Author, Book
from django.utils import timezone

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date']



class BookSerializer(serializers.ModelSerializer):
     authors = AuthorSerializer(many=True, read_only=True)
    author_name = serializers.CharField(source = 'author.name', read_only=True)

    class Meta:
        model = Book
        fields =['id', 'title', 'author', 'author_name', 'published_date', 'isbn']


    def validate_published_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("The published date cannot be in the future.")
            return value
~                                                                                                                                                    
~                        
