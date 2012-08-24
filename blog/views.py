from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from django.shortcuts import render
from django.contrib.auth.models import User

from blog.models import Post

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render(request, "blog/tagpage.html", {"posts":posts, "tag":tag})

def post_detail(request, slug):
    blog_post = get_object_or_404(BlogPost.objects.filter())
