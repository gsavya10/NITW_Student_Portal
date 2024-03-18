"""StudentPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from StudentPortal.rest import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls')),
    path('results/', include('results.urls')),
    path('attendance/', include(('attendance.urls', 'attendance'), namespace='attendance')),
    path('feedback/', include(('feedback.urls', 'feedback'), namespace='feedback')),
    path('openelective/', include(('open_elective.urls', 'open_elective'), namespace='open_elective')),
    path('', include('studentdata.urls')),
]
