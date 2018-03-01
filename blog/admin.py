from django.contrib import admin
from .models import Bucket, Post
from django.db import models
from pagedown.widgets import AdminPagedownWidget

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }


class BucketAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

    class Meta:
        model = Bucket

admin.site.register(Bucket, BucketAdmin)
admin.site.register(Post, PostAdmin)
