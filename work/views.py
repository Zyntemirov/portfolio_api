import json
from django.core import serializers

from django.http import JsonResponse

from .models import Work

def get_works(request):
    works = Work.objects.all()
    json_works = serializers.serialize('json', works)
    json_works = json.loads(json_works)

    return JsonResponse({'work': json_works})

