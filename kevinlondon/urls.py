from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import redirect_to
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', redirect_to, {'url': '/blog/'}),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^about/', include('about.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
  
