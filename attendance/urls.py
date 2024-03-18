from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
	path(r'', views.viewAttendance, name='viewAttendance'),
]
