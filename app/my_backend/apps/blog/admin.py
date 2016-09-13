from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import BlogPost


class BlogPostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'slug', 'draft', 'posted_at')


admin.site.register(BlogPost, BlogPostAdmin)
