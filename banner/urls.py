from django.urls import path
from .views import *

urlpatterns = [
    path('', list_banner_photo),
]
