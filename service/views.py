from rest_framework import viewsets
from service.serializers import ServiceSerializer, SuccessSerializer

from service.models import Service, Success

class ServicesAllView(viewsets.generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

# class ServicesUpdateView(viewsets.generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ServiceSerializer
#     queryset = Service.objects.all()

class SuccessView(viewsets.generics.ListCreateAPIView):
    serializer_class = SuccessSerializer
    queryset = Success.objects.all()
