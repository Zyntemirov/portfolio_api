from django.urls import path,include
from service.views import *

urlpatterns = [
    path('', ServicesAllView.as_view()),
    # path('edit/<int:pk>/', ServicesUpdateView.as_view()),
    path('success/', SuccessView.as_view()),
]
