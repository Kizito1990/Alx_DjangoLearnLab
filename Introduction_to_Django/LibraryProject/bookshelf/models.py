from django.db import models
from contrib.utils import admin

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()



    def __str__(self):
        return self.title

    class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publication_year"]

