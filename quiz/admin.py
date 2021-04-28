from django.contrib import admin
from .models import Question, Category
from .forms import QuestionForm
from .list_filters import QuestionListFilter

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    list_filter = (QuestionListFilter,)

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)