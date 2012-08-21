from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView
from blog.models import Post

urlpatterns = patterns('blog.views',
    url(r'^$', ListView.as_view(
                 queryset=Post.objects.all().order_by("-created"),
                 template_name="blog/list.html")),
)
