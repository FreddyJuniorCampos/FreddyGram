"""Posts admin classes."""


# Django
from django.contrib import admin


# Models
from posts.models import Post


@admin.register(Post)
class Posts(admin.ModelAdmin):
    """Post admin."""

    list_display = ('pk', 'profile', 'user', 'title', 'photo')
