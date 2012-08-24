from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView

urlpatterns = patterns('',
    url(r'^$', DetailView.as_view(template_name="about.html"))
)
