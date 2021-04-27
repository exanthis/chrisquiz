from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers
from quiz.models import Question

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('ignore_until',)

    def update(self, instance, validated_data):
        print('hello')
        if self.context['request'].query_params.get('days'):
            print('in queryparamsif')
            days = int(self.context['request'].query_params['days'])
            until = timezone.now() + timedelta(days=days)
            instance.ignore_until = until
            instance.save()
            return instance
        else:
            # No query param ?vote
            raise serializers.ValidationError({
                '?days=<int:days>': 'You must provide query parameters for days, as in integer.',
            })            
