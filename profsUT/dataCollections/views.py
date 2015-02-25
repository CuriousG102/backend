from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404, render
from django.views import generic
from django.views.generic import TemplateView
from dataCollections.forms import ResponseForm
from dataCollections.models import Instructor
from dataCollections.models import Course
from dataCollections.models import CourseTime
from dataCollections.models import Question
from dataCollections.models import Response


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

# class InstructorView(generic.DetailView):
#     model = Instructor
#     template_name = "instructor.html"

#     def get_object(self):
#         return get_object_or_404(Instructor, pk=request.session['teacher_id'])

def instructorView(request, teacher_id):
    instructor = get_object_or_404(Instructor, pk=teacher_id)
    print request

    return render(request, 'instructor.html', {
        'instructor': instructor,
        'error_message': "No such professor.",
    })

def submit(request, teacher_id):
    instructor = get_object_or_404(Instructor, pk=teacher_id)
    # question = request.POST['question']
    # print request.POST['question']
    print request
    print instructor.first

    # try:
        # selected_instructor = instructor.get(pk=request.POST['instructor'])
    # except (KeyError, Instructor.DoesNotExist):
        # Redisplay the poll voting form.
    return render(request, 'response.html', {
        'instructor': instructor,
        'error_message': "No such professor.",
    })

    print 'blablba'
    # selected_choice.votes += 1
    # selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('dataCollections:afterSubmit', args=(instructor.id,)))

# def submitResponse(request):
#     if request.method == 'POST':
#         form = ResponseForm(request.POST)
#         if form.is_valid():
#             _question = form.cleaned_data['question']
#             _response = form.cleaned_data['response']
#             _instructor = form.cleaned_data['instructor']

#             new_question = Question.objects.get(pk=1)

#             new_instructor = Instructor.objects.get(pk=1)

#             new_response = Response()
#             new_response.response = _response
#             new_response.question = new_question
#             new_response.instructor = new_instructor
#             new_response.save()

#             return render_to_response('response.html', {}, context_instance=RequestContext(request))
#     else:
#         form = ResponseForm()
#     return render_to_response('index.html', {'response': form}, context_instance=RequestContext(request))
