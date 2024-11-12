from .forms import ExampleForm
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from . models import Book
# Create your views here.

@permission_required('bookshelf.can_view', raise_exception = True)
def can_view(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    return render(request, 'bookshelf/list_book.html',{' book':book}




@permission_required('bookshelf.can_edit', raise_exception=True)
def can_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def can_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})


@permission_required('bookshelf.can_create', raise_exception = True)
def can_create(request, title, author, publication date,  book_id):
    book = Book(title ='title', author = 'author, publucation_date = 'publication_date')
    book.save()
    return render(request, 'bookshelf/list_book.html',{' book':book}




# Example of using ORM for secure queries
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

def search_books(request):
    query = request.GET.get('q')
    if query:
        # Using ORM filter with parameterized queries to prevent SQL injection
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
