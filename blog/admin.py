from django.contrib import admin
from .models import Post
from django.db import models
from pagedown.widgets import AdminPagedownWidget

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Post, PostAdmin)
