from django.db import models
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

    date_created = models.DateField()
    date_updated = models.DateTimeField(auto_now=True)
