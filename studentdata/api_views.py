from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from .serializers import *
from StudentPortal.rest.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import Http404


class UserViewSet(viewsets.ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAuthenticated, )


class StudentDataViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
	queryset = StudentData.objects.all()
	serializer_class = StudentDataSerializer
	permission_classes = (IsAuthenticated, )

	def list(self, request, *args, **kwargs):
		instance = get_object_or_404(self.get_queryset(), userid=request.user.id)
		serializer = self.get_serializer(instance)
		return Response(serializer.data)

