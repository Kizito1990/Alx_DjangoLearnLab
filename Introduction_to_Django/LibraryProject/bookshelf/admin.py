from django.contrib import admin
from .models import Book

admin.site.register(Book)

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publication_year"]


class BookAdmin(admin.ModelAdmin):
    list_filter = ["title", "author", "publication_year"]
