from rest_framework import generics
from quiz.models import Question
from .serializers import QuestionSerializer

class IgnoreQuestion(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
