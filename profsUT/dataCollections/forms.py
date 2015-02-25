from django import forms
from models import Instructor, Course, CourseTime, Question, Response

class ResponseForm(forms.ModelForm):
    question = forms.CharField(max_length=1000, help_text="Please describe your course")
    text = forms.CharField(max_length=1000, help_text="Please describe your course")
    text = forms.CharField(max_length=1000, help_text="Please describe your course")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Response
