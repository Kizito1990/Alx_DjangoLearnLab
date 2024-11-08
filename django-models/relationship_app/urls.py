from django.urls import path
from .views import list_books, LoginView, LogoutView, register


urlpatterns = [
    path('', views.list_books, name='list_books'),  
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name = 'login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.hyml"), name='logout'),
    path('register/', views.register, name='register'),

]
