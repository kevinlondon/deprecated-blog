from django.conf.urls.defaults import patterns, url

# Blog patterns
urlpatterns = patterns('blog.views',
    url(r'^$', 'blog_post_list'),
)
