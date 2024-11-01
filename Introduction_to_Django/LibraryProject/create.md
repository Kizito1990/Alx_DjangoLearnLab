#!/bin/bash
#import models.py file from the bookshelf app
from bookshelf.models import Book

#creating of an instance of the Book model
book =  Book(title = '1984', author = 'George Orwell', publication_year = 1949)
book.save()
#The outcome of the command is that object of the Book model will be created in the database table
