from django.conf.urls import patterns, include, url
from django.contrib import admin
import views


urlpatterns = patterns('',
    url(r'^view/(?P<teacher_id>\d+)$', views.instructorView, name='profView'),
    url(r'^thankyou/', views.thankYou, name='thankYou'),
    url(r'^$', views.home, name='home'),
)
