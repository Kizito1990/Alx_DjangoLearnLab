from django.urls import path
from .views import list_books, LoginView, LogoutView, register


urlpatterns = [
    path('', views.list_books, name='list_books'),  
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.hyml"), name='logout'),
    path('register/', views.register, name='register'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),

]
