from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dataCollections import views

urlpatterns = (
	url(r'^api/instructors/$', views.InstructorList.as_view()),
	url(r'^api/instructors/(?P<pk>[0-9]+)/$', views.InstructorDetail.as_view()),
	url(r'^api/courses/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view()),
)