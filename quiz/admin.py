from django.contrib import admin
from .models import Question, Category
from .forms import QuestionForm

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)