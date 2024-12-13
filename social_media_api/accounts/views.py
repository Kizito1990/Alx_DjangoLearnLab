from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import CustomUser
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        followuser = get_object_or_404(CustomUser, id=user_id)
        if request.user.is_following(followuser):
            return Response({'detail': 'You are already following this user.'}, status=400)
        request.user.follow(followuser)
        return Response({'detail': f'You are now following {followuser.username}.'})

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        unfollowuser = get_object_or_404(CustomUser, id=user_id)
        if not request.user.is_following(unfollowuser):
            return Response({'detail': 'You are not following this user.'}, status=400)
        request.user.unfollow(unfollowuser)
        return Response({'detail': f'You have unfollowed {unfollowuser.username}.'})

