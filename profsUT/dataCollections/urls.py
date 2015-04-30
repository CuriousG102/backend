from django.conf.urls import patterns, include, url
from django.contrib import admin
from dataCollections import views


urlpatterns = patterns('',
    # took Zac's forms out until he fixes them
    # url(r'^view/(?P<teacher_id>\d+)$', views.instructorView, name='profView'),
    # url(r'^thankyou/', views.thankYou, name='thankYou'),
    url(r'^api/instructors/$', views.InstructorList.as_view()),
	url(r'^api/instructors/(?P<pk>[0-9]+)/$', views.InstructorDetail.as_view()),
	url(r'^api/courses/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view()),
    url(r'^api/courses/$', views.CourseList.as_view()),
    url(r'^api/videos/$', views.VideoList.as_view()),
)
