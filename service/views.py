import json
from django.core import serializers

from django.http import JsonResponse

from .models import Service, Success

def get_services(request):
    services = Service.objects.all()
    json_services = serializers.serialize('json', services)
    json_services = json.loads(json_services)

    return JsonResponse({'services': json_services})

def get_success(request):
    success = Success.objects.all()
    json_success = serializers.serialize('json', success)
    json_success = json.loads(json_success)

    return JsonResponse({'services': json_success})
