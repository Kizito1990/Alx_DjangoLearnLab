from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {"books":books}
    return render(request, "book/list_books.html", context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'book/library_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(self, **kwargs)
        context['library_list'] = Library.books.all()
        return context

    
