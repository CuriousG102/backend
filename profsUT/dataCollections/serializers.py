from django.db.models import Avg

from rest_framework import serializers
from dataCollections.models import Instructor, Course, CourseTime, Question, Response, CIS
from videos.serializers import VideoSerializer

class ResponseSerializer(serializers.ModelSerializer):
    question = serializers.ReadOnlyField(source='question.text')
    class Meta:
        model = Response
        fields = ('text', 'question')

class CourseLessDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'courseID', 'courseName', 'semesterYear', 
                  'semesterSeason')

class CourseTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTime
        fields = ('m', 't', 'w', 'th', 'f', 's',
                  'su', 'time', 'endTime',)

class CourseSerializer(serializers.ModelSerializer):
    times = CourseTimeSerializer(many = True, read_only=True)

    class Meta:
        model = Course
        depth = 1
        fields = ('courseID', 'courseName', 'uniqueNo',
                  'syllabus', 'instructor', 'inst_provided_description',
                  'reg_provided_description', 'semesterSeason', 
                  'semesterYear', 'times')

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        depth = 1
        fields = ('id', 'courseID', 'courseName', 'semesterYear',
                  'semesterSeason', 'instructor')

def instructor_rating_average(self, instructor):
    avgDict = CIS.objects.filter(instructor=instructor).aggregate(Avg('instructor_was_average'))
    return avgDict['instructor_was_average__avg']

class InstructorListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField(method_name='instructor_rating_average')
    courses = CourseLessDetailSerializer(many = True, read_only=True)

    class Meta:
        model = Instructor
        fields = ('id', 'last', 'first', 'courses', 'profile_photo', 'average_rating')

    instructor_rating_average = instructor_rating_average

class InstructorDetailSerializer(InstructorListSerializer):
    average_rating = serializers.SerializerMethodField(method_name='instructor_rating_average')
    responses = ResponseSerializer(many = True, read_only=True)
    courses = CourseSerializer(many = True, read_only=True)
    video = VideoSerializer(many = True, read_only=True)

    class Meta:
        model = Instructor
        fields = ('id', 'last', 'first', 'courses', 'profile_photo', 'bio', 'responses', 'video', 'average_rating')

    instructor_rating_average = instructor_rating_average

