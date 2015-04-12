from django.conf.urls import patterns, include, url
from django.contrib import admin


from dataCollections import urls

import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'profsUT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^profsUT/', include('dataCollections.urls', namespace="dataCollections")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
   							   namespace='rest_framework')),
    url(r'^videos/', include('videos.urls', namespace="videos"))
)
if False:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)