from django.conf.urls.defaults import patterns, url

# Blog patterns
urlspatterns = patterns("blog.views",
    url(r"^$", "blog_post_list"),
)
