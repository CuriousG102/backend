from django import forms
from models import Instructor, Course, CourseTime, Question, Response


class ResponseForm(forms.Form):

    courseId = forms.CharField(max_length=10, label="Course Code")
    courseName = forms.CharField(max_length=100, label="Course Name")
    courseDescription = forms.CharField(max_length = 1000, widget=forms.Textarea, label="Course Description")
