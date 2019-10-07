from django.urls import path
from .views import *

urlpatterns = [
    path('', get_services),
    path('success', get_success),
]
