from rest_framework import serializers
from service.models import Service, Success

class ServiceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Service
        fields = '__all__'


class SuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Success
        fields = '__all__'