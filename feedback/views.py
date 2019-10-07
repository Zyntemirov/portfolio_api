import json
from django.core import serializers

from django.http import JsonResponse

from .models import Feedback

def get_feedbacks(request):
    feedbacks = Feedback.objects.all()
    json_feedbacks = serializers.serialize('json', feedbacks)
    json_feedbacks = json.loads(json_feedbacks)

    return JsonResponse({'feedbacks': json_feedbacks})