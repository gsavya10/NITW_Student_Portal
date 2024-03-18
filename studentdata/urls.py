from django.conf.urls import url,include
from django.urls import path
from . import views
from django.contrib.auth.views import auth_logout
from rest_framework.routers import DefaultRouter
from .api_views import *

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('studentdata', StudentDataViewSet)

#app_name = 'info'
urlpatterns = [
	url(r'^$',views.mLogin),
	url(r'^logout/$', views.mLogout),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^editProfile/$', views.editProfile, name='editProfile'),
	url(r'^activate/(?P<arg>[\w\-]+)/$', views.activateUser, name='activateUser'),
	url(r'^changePassword/$', views.changePassword, name='changePassword'),
	url(r'^amnesiac/$', views.forgotPassword, name='forgotPassword'),
]