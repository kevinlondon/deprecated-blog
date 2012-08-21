from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView
from blog.models import BlogPost
# Blog patterns
urlpatterns = patterns('blog.views',
    url(r'^$', ListView.as_view(
        queryset=BlogPost.objects.all().order_by("-created")[:2],
        template_name="blog/list.html")),
)
