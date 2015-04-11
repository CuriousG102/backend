from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from dataCollections.forms import ResponseForm
from django.forms.formsets import formset_factory, BaseFormSet
from dataCollections.models import Instructor, Course, Question, Response
from dataCollections.serializers import InstructorListSerializer, InstructorDetailSerializer, CourseSerializer
from rest_framework import generics

def instructorView(request, teacher_id):
    # This class is used to make empty formset forms required
    # See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    instructor = get_object_or_404(Instructor, pk=teacher_id)
    questions = Question.objects.filter()
    # data = {'question1': questions[1].text }
    form = ResponseForm()

    CourseFormSet = formset_factory(ResponseForm, max_num=10, formset=RequiredFormSet)

    if request.method == 'POST':
        form = ResponseForm(request.POST)
        course_info_form = ResponseForm(request.POST)
        # Create a formset from the submitted data
        course_info_formset = CourseFormSet(request.POST, request.FILES)
        print course_info_form.errors
        if course_info_formset.is_valid():
            print "Valid form"
            print course_info_formset.forms
            for counter, form in enumerate(course_info_formset.forms):
                # print request
                # Save courses here and redirect
                instructor = get_object_or_404(Instructor, pk=teacher_id)
                print request.POST['form-'+str(counter)+'-courseId']
                courseId = request.POST['form-'+str(counter)+'-courseId']
                courseName = request.POST['form-'+str(counter)+'-courseName']
                courseDescription = request.POST['form-'+str(counter)+'-courseDescription']
                course = Course(instructor=instructor, courseID=courseId, courseName=courseName, inst_provided_description=courseDescription)
                course.save()
            return HttpResponseRedirect('/profsUT/thankyou/')
    else:
        form = ResponseForm()
        course_info_form = ResponseForm()
        course_info_formset = CourseFormSet()

    return render(request, 'instructor.html', {
        'form': course_info_form,
        'formset': course_info_formset,
        'instructor': instructor,
        'questions': questions,
        'error_message': "No such professor.",
    })


def thankYou(request):
    return render(request, 'afterSubmit.html', {

    })

class InstructorList(generics.ListAPIView):
	queryset = Instructor.objects.all().prefetch_related('courses')
	serializer_class = InstructorListSerializer

class InstructorDetail(generics.RetrieveAPIView):
	queryset = Instructor.objects.all()
	serializer_class = InstructorDetailSerializer

class CourseDetail(generics.RetrieveAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
