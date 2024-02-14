from rest_framework import generics, permissions

from .models import Post
from .permissions import IsAuthOrReadOnly
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) view level permission set
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,) view level permission set
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
