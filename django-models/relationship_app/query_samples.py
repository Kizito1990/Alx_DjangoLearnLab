from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author
author = Author.objects.get(name=author_name)

# List all books in a library
library = Library.Book.objects.all()

# Retrieve the librarian for a library
library = Library.Librarian.objects.all()
