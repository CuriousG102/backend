from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404, render
from django.views import generic
from django.views.generic import TemplateView
from dataCollections.forms import ResponseForm
from dataCollections.models import Instructor, Course, CourseTime, Question, Response

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('dataCollections/index.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))

def home(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))

def instructorView(request, teacher_id):
    instructor = get_object_or_404(Instructor, pk=teacher_id)
    questions = Question.objects.filter()
    data = {'question1': questions[1].text }
    form = ResponseForm(initial=data)

    if request.method == 'POST':
        print request.POST
        form = ResponseForm(request.POST)
        response1 = request.POST['response1']
        response2 = request.POST['response2']
        question1 = request.POST['question1']
        question2 = request.POST['question2']
        if form.is_valid():
            instructor = get_object_or_404(Instructor, pk=teacher_id)
            responseObj = Response.objects.filter(instructor=instructor)
            # Change this
            if len(responseObj) == 0:
                r1 = Response(instructor=instructor, text=response1, question=Question.objects.get(pk=question1))
                r1.save()
                r2 = Response(instructor=instructor, text=response2, question=Question.objects.get(pk=question2))
                r2.save()

            return HttpResponseRedirect('/profsUT/thankyou/')
    else:
        form = ResponseForm(initial = data)

    return render(request, 'instructor.html', {
        'form': form,
        'instructor': instructor,
        'questions': questions,
        'error_message': "No such professor.",
    })


def thankYou(request):
    return render(request, 'afterSubmit.html', {

    })
