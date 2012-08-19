from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from blog.models import BlogPost

def blog_post_list(request):
    """Main listing of blog posts."""
    posts = BlogPost.objects.all.order_by("-created")
    paginator = Paginator(posts, 2)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render("blog/list.html", dict(posts=posts, user=request.user))
