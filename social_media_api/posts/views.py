from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from .models import Post, Like
from notifications.models import Notification

from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        data = [{'id': post.id, 'author': post.author.username, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts]
        return Response(data)


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = generics.get_object_or_404(Post, pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user has already liked the post
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"detail": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new like
        Like.objects.create(user=request.user, post=post)

        # Generate a notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post,
        )

        return Response({"detail": "Post liked successfully"}, status=status.HTTP_201_CREATED)




class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = generics.get_object_or_404(Post, pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the like exists
        try:
            like = Like.objects.get_or_create(user=request.user, post=post)
        except Like.DoesNotExist:
            return Response({"detail": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the like
        like.delete()
        return Response({"detail": "Post unliked successfully"}, status=status.HTTP_200_OK)

