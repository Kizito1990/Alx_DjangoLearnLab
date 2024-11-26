from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        self.Author

class Book(models.Model):
    title = models.CharField(max_length= 50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.DateField()

    def __str__(self) -> str:
        return self.title
~
