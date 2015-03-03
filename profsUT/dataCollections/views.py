from django.shortcuts import render

# Create your views here.

from dataCollections.models import Instructor, Course
from dataCollections.serializers import InstructorListSerializer, InstructorDetailSerializer, CourseSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User

class InstructorList(generics.ListAPIView):
	queryset = Instructor.objects.all()
	serializer_class = InstructorListSerializer

class InstructorDetail(generics.RetrieveAPIView):
	queryset = Instructor.objects.all()
	serializer_class = InstructorDetailSerializer

class CourseDetail(generics.RetrieveAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer