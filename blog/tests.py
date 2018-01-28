from datetime import datetime
from django.test import TestCase

from .models import Post


class BlogTestCase(TestCase):
    def test_can_save_post(self):
        post = Post()
        post.title = 'Hello to blogging'
        post.content = 'This is my introduction'
        post.date_created = datetime.now()
        post.date_update = None
        post.published = True
        post.tags = ['introduction',]
        post.slug = '2018-01-01-happy-new-year'
        post.save()

        self.assertEqual(1, Post.objects.count())
        self.assertEqual(
            'Hello to blogging',
            Post.objects.first().title,
        )
