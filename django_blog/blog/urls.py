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


    path('post/<int:pk>/comments/new/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),


    path('search/', views.post_search, name='post_search'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
    path('tags/<slug:tag_slug>/',PostByTagListView.as_view()),
]

