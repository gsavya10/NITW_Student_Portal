from django.conf.urls import url,include
from . import views
from django.urls import path
from django.contrib.auth.views import auth_logout

from rest_framework.routers import DefaultRouter
from .api_views import *

router = DefaultRouter()
router.register('results', ResultsViewSet)


urlpatterns = [
    path('', views.index),
]