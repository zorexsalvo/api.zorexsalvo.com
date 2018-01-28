from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """A viewset for retrieving posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
