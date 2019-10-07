import json
from django.core import serializers

from django.http import JsonResponse

from .models import Blog

def get_blogs(request):
    blog = Blog.objects.all()
    json_blog = serializers.serialize('json', blog)
    json_blog = json.loads(json_blog)

    return JsonResponse({'blogs': json_blog})