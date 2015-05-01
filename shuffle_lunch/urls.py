from django.conf.urls import url, include, patterns

from . import views

from .api import ShuffleResource

shuffle_resource = ShuffleResource()


urlpatterns = patterns('',
    (r'^api/', include(shuffle_resource.urls)),
    url(r'^$', views.index, name='index'),
)