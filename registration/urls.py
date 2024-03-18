from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from .api_views import *

router = DefaultRouter()
router.register('registration', RegistrationViewSet)

urlpatterns = [
    path('', views.index),
    path('payment/', views.getMessInfo),
]