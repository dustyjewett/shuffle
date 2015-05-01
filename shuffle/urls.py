from django.conf.urls import patterns, include, url
from django.contrib import admin

    # Examples:
    # url(r'^$', 'shuffle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
urlpatterns = patterns('',
    url('^', include('django.contrib.auth.urls')),
    url(r'^shuffle/', include('shuffle_lunch.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
