from django.conf.urls import patterns, include, url
from django.contrib import admin
from dataCollections import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'profsUT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^profsUT/', include('dataCollections.urls', namespace="dataCollections")),
    url(r'^admin/', include(admin.site.urls)),
)
