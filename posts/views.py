from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer, UserSerializer # new
from .permissions import IsAuthorOrReadOnly # new
from django.contrib.auth import get_user_model # new
from rest_framework import viewsets # new
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class UserList(generics.ListCreateAPIView):  # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class =  UserSerializer    