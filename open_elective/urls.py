from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
	path('', views.viewInstructions, name='viewInstructions'),
	path('prefer', views.viewApplications, name='viewApplications'),
	path('submit', views.storeChoices, name='storeChoices'),
]
