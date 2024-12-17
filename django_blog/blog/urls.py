from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, profile_view, PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


    path('posts/<int:post_id>/comments/new/', views.add_comment, name='add_comment'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]

