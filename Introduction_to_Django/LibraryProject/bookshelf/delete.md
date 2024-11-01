
#!/bin/bash
from bookshelf.models import Book

book = Book.objects.all()
book.delete()

#The book instances was deleted after the python command
(1, {'bookshelf.Book': 1})


Book.objects.all()
<QuerySet []>

