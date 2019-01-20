from .models import Question


def get_questions(request):
    question_list = Question.objects.order_by('pub_date')
    return {
        'question_list': question_list,
    }
