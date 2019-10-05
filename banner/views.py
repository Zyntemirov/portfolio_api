import json
from django.core import serializers

from django.http import JsonResponse

from .models import Banner

def list_banner_photo(request):
    banner = Banner.objects.all()
    json_banner = serializers.serialize('json', banner)
    json_banner = json.loads(json_banner)

    return JsonResponse({'banner_photos': json_banner})