from django.contrib import admin

from blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    """Admin class for blog posts."""
    search_fields = ["title"]

admin.site.register(BlogPost, BlogPostAdmin)
