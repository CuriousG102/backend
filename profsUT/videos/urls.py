from django.conf.urls import patterns, include, url
from django.contrib import admin
from videos import views

urlpatterns = patterns('',
    url(r'^webhook/heywatch/(?P<video_id>\d+)$', 
        views.heyWatchPost, name='heyWatchHook'),
)