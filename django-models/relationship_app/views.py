from django.shortcuts import render, redirect
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {"books":books}
    return render(request, "relationship_app/list_books.html", context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(self, **kwargs)
        context['library'] = Library.books.all()
        return context

# Login view
class LoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True

# Logout view
class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Adjust 'home' to your app's homepage or desired redirection.
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})    
