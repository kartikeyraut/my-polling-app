from django.shortcuts import get_object_or_404,render 
from django.http import HttpResponse , HttpResponseRedirect
from .models import Choice , Question
from django.template import loader
from django.http import Http404 # for detail()
from django.urls import reverse
from django.views import generic
#Create your views here. 


#abhi apan banyege genrec view
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'






# from django.shortcuts import render
#from .models import Question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
#render function request object lega , template lega , dictionary optional lega aur render karke HttpResponse return karega


# def index(request):
#     latest_question_list=Question.objects.order_by('-pub_date')[:5]
    
#     template = loader.get_template('polls/index.html') #polls/index.html is basically polls/templates/polls/index.html
#     context = {
#         'latest_question_list': latest_question_list,
#     }
    
#     return HttpResponse(template.render(context,request))

# def index(request): 
#     return HttpResponse("Hello, world. You're at the poll's index.")


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
#ye func Http404 return karega agar question does not exist

#upar wale ke liye django me shortcut hota hai 
# as described below
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
# get_object_or_404() , model aur ek argument lega jisko wo get() function  of models manager ko pass karega to agar question exist nahi karega to Http4 error aayega


#aur ek get_list_or_404 function hota hai , jo filter() use karega instead of get() , aur Http404 raise karega if the list is empty



# Philosophy

# Why do we use a helper function get_object_or_404() instead of automatically catching the ObjectDoesNotExist exceptions at a higher level, or having the model API raise Http404 instead of ObjectDoesNotExist?

# Because that would couple the model layer to the view layer. One of the foremost design goals of Django is to maintain loose coupling. Some controlled coupling is introduced in the django.shortcuts module.








def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # error aayega to question voting form phr se diaplay karenge.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
    
    
    
    
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})    