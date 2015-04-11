from rest_framework import serializers
from dataCollections.models import Instructor, Course, CourseTime, Question, Response

class ResponseSerializer(serializers.ModelSerializer):
    question = serializers.ReadOnlyField(source='question.text')
    class Meta:
        model = Response
        fields = ('text', 'question')

class CourseLessDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'courseID', 'courseName', 'semesterYear')

class InstructorListSerializer(serializers.ModelSerializer):
    courses = CourseLessDetailSerializer(many = True, read_only=True)

    class Meta:
        model = Instructor
        fields = ('id', 'last', 'first', 'courses', 'profile_photo')

class InstructorDetailSerializer(InstructorListSerializer):
    responses = ResponseSerializer(many = True, read_only=True)

    class Meta:
        model = Instructor
        fields = ('id', 'last', 'first', 'courses', 'profile_photo', 'bio', 'responses')

class CourseTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTime
        fields = ('m', 't', 'w', 'th', 'f', 's', 'su',
                  'time', 'endTime')

class CourseSerializer(serializers.ModelSerializer):
    times = CourseTimeSerializer(many = True, read_only=True)

    class Meta:
        model = Course
        fields = ('courseID', 'courseName', 'uniqueNo',
                  'syllabus', 'instructor', 'inst_provided_description',
                  'reg_provided_description', 'semesterSeason', 
                  'semesterYear', 'times')