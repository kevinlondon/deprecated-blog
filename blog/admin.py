from django.contrib import admin

from blog.models import Post

class BlogPostAdmin(admin.ModelAdmin):
    """Admin class for blog posts."""
    search_fields = ["title"]

admin.site.register(Post, BlogPostAdmin)
