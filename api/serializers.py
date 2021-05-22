from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers
from quiz.models import Question

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('ignore_until',)

    def update(self, instance, validated_data):
        if self.context['request'].query_params.get('days'):
            print('in queryparamsif')
            if self.context['request'].query_params.get('days') == 'indefinitely':
                instance.hide_indefinitely = True
            else:
                days = int(self.context['request'].query_params['days'])
                until = timezone.now() + timedelta(days=days)
                print(f"ignoring until {until}")
                instance.ignore_until = until
            instance.save()
            return instance
        else:
            # No query param ?vote
            raise serializers.ValidationError({
                '?days=<int:days>': 'You must provide query parameters for days, as in integer.',
            })            
