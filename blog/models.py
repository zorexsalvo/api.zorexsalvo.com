from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = ArrayField(
        models.CharField(max_length=255, blank=True),
        size=8,
    )
    published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50)
    cover_image = models.ImageField(upload_to='uploads/')
    short_description = models.TextField()

    date_created = models.DateField()
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.slug
