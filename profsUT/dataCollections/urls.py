from django.conf.urls import patterns, include, url
from django.contrib import admin
import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'profsUT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^view/(?P<teacher_id>\d+)$', views.instructorView, name='profView'),
    url(r'^submit/(?P<teacher_id>\d+)$', views.submit, name='submit'),
    url(r'^$', views.home, name='home'),
    # url(r'^dataCollections/', include(admin.site.urls)),
)
