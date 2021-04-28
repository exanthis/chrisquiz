from django import forms
from .models import Category, Question


class QuestionFilterForm(forms.Form):
    categories = Category.objects.all()
    CATEGORY_CHOICES = []
    for category in categories:
        CATEGORY_CHOICES.append((category.id, category.name,))

    number_of_questions = forms.IntegerField(label="Number of questions", required=True, initial=10)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), to_field_name="id", required=False, help_text="You can leave this blank")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # UI elements
        self.fields['number_of_questions'].widget.attrs.update({'class': 'form-control form-control-sm' })
        self.fields['categories'].widget.attrs.update({'class': 'form-control form-control-sm' })

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'category': forms.RadioSelect(),
        }
