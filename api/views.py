from rest_framework import generics
from quiz.models import Question
from .serializers import QuestionSerializer

class IgnoreQuestion(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    #def get_queryset(self):
    #    pk = self.kwargs['pk']
    #    print(Question.objects.get(pk=pk))
    #    return Question.objects.get(pk=pk)