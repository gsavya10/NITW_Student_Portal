from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'feedback', views.RegisteredCoursesViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('', views.feedback_home, name='feedback_home'),
    path('fill_feedback/<slug:courseID>', views.fill_feedback, name='fill_feedback'),
    path('submit_feedback/<slug:courseID>', views.submit_feedback, name='submit_feedback'),
    # path('feedback', views.FeedbackViewSet)
]