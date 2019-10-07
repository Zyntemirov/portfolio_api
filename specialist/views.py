import json
from django.core import serializers

from django.http import JsonResponse

from .models import Specialist, Skill

def get_specialist(request):
    specialist = Specialist.objects.all()
    json_specialist = serializers.serialize('json', specialist)
    json_specialist = json.loads(json_specialist)

    skills = Skill.objects.filter(specialist=json_specialist[0]['pk'])
    json_skills = serializers.serialize('json', skills)
    json_skills = json.loads(json_skills)

    json_specialist[0]['fields']['skills'] = json_skills

    return JsonResponse({'specialist': json_specialist})