from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
	is_student = serializers.SerializerMethodField()

	class Meta:
		model = Users
		fields = ('username', 'email', 'first_name', 'middle_name', 'last_name', 'company', 'phone', )

	def get_is_student(self, instance):
		return StudentData.objects.filter(userid=instance.id).exists()


class StudentDataSerializer(serializers.ModelSerializer):

	class Meta:
		model = StudentData
		fields = '__all__'

