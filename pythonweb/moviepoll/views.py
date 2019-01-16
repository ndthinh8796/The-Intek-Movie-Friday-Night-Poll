from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    question_list = Question.objects.order_by('pub_date')
    return render(request,
                  'moviepoll/index.html',
                  {'question_list': question_list},
                  )


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,
                  'moviepoll/detail.html',
                  {'question': question},
                 )


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'moviepoll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('moviepoll:detail', args=[question.id]))
