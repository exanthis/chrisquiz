from datetime import timedelta
from django.contrib import admin
from django.utils import timezone
from .models import Question, Category
from .forms import QuestionForm
from .list_filters import QuestionIgnoredListFilter


@admin.action(description="Remove 'ignore' on selected questions")
def unignore(modeladmin, request, queryset):
    queryset.update(ignore_until=timezone.now())

@admin.action(description="Ignore selected questions for 7 days")
def ignore_for_seven_days(modeladmin, request, queryset):
    queryset.update(ignore_until=timezone.now() + timedelta(days=7))

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    list_filter = ('category', QuestionIgnoredListFilter,)
    actions = (unignore, ignore_for_seven_days)

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)