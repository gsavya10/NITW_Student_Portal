from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from .serializers import *
from StudentPortal.rest.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import Http404
from studentdata.models import StudentData


class RegistrationViewSet(viewsets.ModelViewSet):
	queryset = Registered.objects.all()
	serializer_class = RegisteredSerializer
	permission_classes = (IsAuthenticated, )

	def list(self, request):
		user = request.user
		student_data = StudentData.objects.get(userid=user.id)
		result_list = self.get_queryset().filter(registration_number=student_data.registration_number)
		serializer = self.serializer_class(result_list, many=True)
		return Response(serializer.data)

