#!/bin/bash
from bookshelf.models import Book

book = Book.objects.all()[0]
book.title = "Nineteen Eighty-Four"
book.save()

#The title column was changed from 1984 to Nineteen Eighty-Four

