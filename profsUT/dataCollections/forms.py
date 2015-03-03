from django import forms
from models import Instructor, Course, CourseTime, Question, Response


class ResponseForm(forms.Form):
  qs = Question.objects.filter()

  # make this more pythonic / get values from db
  QUESTIONS = (
      (1, qs[0].text),
      (2, qs[1].text),
  )

  question1 = forms.ChoiceField(choices=QUESTIONS, label="Question")
  response1 = forms.CharField(widget = forms.Textarea, max_length=2000, label="Response")

  question2 = forms.ChoiceField(choices=QUESTIONS, label="Question")
  response2 = forms.CharField(widget = forms.Textarea, max_length=2000, label="Response")

    # An inline class to provide additional information on the form.
    # class Meta:
        # Provide an association between the ModelForm and a model
        # model = Response
