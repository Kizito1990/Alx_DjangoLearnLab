#!/bin/bash
from bookshelf.models import Book

Book.objects.all()

#Below is the outcome of the python code that feltches all objects of bthe database
<QuerySet [<Book: 1984>]>
