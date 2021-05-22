from django.shortcuts import render
from django.utils import timezone
from .models import Question, Category
from .forms import QuestionFilterForm, QuestionFilterForm1


# Create your views here.
def index(request):
    if request.GET.get('number_of_questions'):
        # Return filter form to user
        form = QuestionFilterForm1(request.GET)
        # Check if user is wanting specific categories
        number_of_questions_requested = int(request.GET.get('number_of_questions'))
        if request.GET.get('categories'):
            categories_requested_by_id = request.GET.getlist('categories')
            # Get number of questions requested
            # Get category instances queryset from db
            categories_in_db = Category.objects.filter(id__in=categories_requested_by_id)
            # Get questions whose categories fall in those selected, randomise,
            # and get only the number of qs specified in the form
            questions = Question.objects.filter(category__in=categories_in_db, hide_indefinitely=False).exclude(ignore_until__gte=timezone.now()).order_by('?')[:number_of_questions_requested]
        else: # User just wants a specified number of questions, doesn't care about category
            questions = Question.objects.exclude(ignore_until__gte=timezone.now()).filter(hide_indefinitely=False).order_by('?')[:number_of_questions_requested]

    else:
        form = QuestionFilterForm1()
        questions = Question.objects.exclude(ignore_until__gte=timezone.now()).filter(hide_indefinitely=False).order_by('?')[:10].select_related('category')
    context = {
        "questions":questions,
        "form": form,
    }
    return render(request, 'quiz/index.html', context)
