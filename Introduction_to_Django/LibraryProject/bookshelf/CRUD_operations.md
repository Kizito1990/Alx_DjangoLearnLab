#!/bin/bash
#Create

from bookshelf.models import Book


book =  Book(title = '1984', author = 'George Orwell', publication_year = 1949)
book.save()

#Retrieve Operation
Book.objects.all()
<QuerySet [<Book: 1984>]>


#update operation
book = Book.objects.all()[0]
book.title = "Nineteen Eighty-Four"
book.save()

#delete operation
book = Book.objects.all()
book.delete()
(1, {'bookshelf.Book': 1})
 Book.objects.all()
<QuerySet []>

