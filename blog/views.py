from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """A viewset for retrieving posts."""

    queryset = Post.objects.filter(published=True).order_by('-date_created')
    serializer_class = PostSerializer
    lookup_field = 'slug'
