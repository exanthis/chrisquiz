from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Question, Category
from .forms import QuestionFilterForm

# Create your views here.
def index(request):
    if request.GET.get('number_of_questions'):
        # Return filter form to user
        filter_form = QuestionFilterForm(request.GET)
        # Check if user is wanting specific categories
        number_of_questions_requested = int(request.GET.get('number_of_questions'))
        if request.GET.get('categories'):
            categories_requested_by_id = request.GET.getlist('categories')
            # Get number of questions requested
            # Get category instances queryset from db
            categories_in_db = Category.objects.filter(id__in=categories_requested_by_id)
            # Get questions whose categories fall in those selected, randomise,
            # and get only the number of qs specified in the form
            questions = Question.objects.filter(category__in=categories_in_db).order_by('?')[:number_of_questions_requested]
        else: # User just wants a specified number of questions, doesn't care about category
            questions = Question.objects.order_by('?')[:number_of_questions_requested]

    else:
        filter_form = QuestionFilterForm()
        questions = Question.objects.order_by('?')[:10].select_related('category')
    context = {
        "questions":questions,
        "filter_form":filter_form,
    }
    return render(request, 'quiz/index.html', context)