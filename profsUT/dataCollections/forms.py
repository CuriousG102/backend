from django import forms
from models import Instructor, Course, CourseTime, Question, Response


class ResponseForm(forms.Form):
    qs = Question.objects.filter()

    # make this more pythonic / get values from db
    QUESTIONS = (
        (1, qs[0].text),
        (2, qs[1].text),
    )

    # question1 = forms.ChoiceField(choices=QUESTIONS, label="Question")
    # response1 = forms.CharField(widget = forms.Textarea, max_length=2000, label="Response")

    courseId = forms.CharField(max_length=10, label="Course Code")
    courseName = forms.CharField(max_length=100, label="Course Name")
    courseDescription = forms.CharField(max_length = 1000, widget=forms.Textarea, label="Course Description")
    # question2 = forms.ChoiceField(choices=QUESTIONS, label="Question")
    # response2 = forms.CharField(widget = forms.Textarea, max_length=2000, label="Response")

    # An inline class to provide additional information on the form.
    # class Meta:
        # Provide an association between the ModelForm and a model
        # model = Response
