from rest_framework import serializers
from .models import *


class StructureSerializer(serializers.ModelSerializer):
	class Meta:
		model = Structure
		fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Courses
		fields = '__all__'

	type_string = serializers.SerializerMethodField()

	def get_type_string(self, instance):
		if instance.type == 1:
			return 'Theory'
		else:
			return 'Lab'


class RegisteredCourseSerializer(serializers.ModelSerializer):

	class Meta:
		model = RegisteredCourses
		fields = '__all__'

	details = serializers.SerializerMethodField()

	def get_details(self, instance):
		return CourseSerializer(Courses.objects.filter(id=instance.course_id), many=True).data


class RegisteredSerializer(serializers.ModelSerializer):

	class Meta:
		model = Registered
		fields = '__all__'

	courses = serializers.SerializerMethodField()
	structure = serializers.SerializerMethodField()
	department = serializers.SerializerMethodField()
	specialization = serializers.SerializerMethodField()

	def get_courses(self, instance):
		return RegisteredCourseSerializer(RegisteredCourses.objects.filter(registered_id=instance.id), many=True).data

	def get_structure(self, instance):
		return StructureSerializer(Structure.objects.filter(id=instance.reg_structure_id).first()).data

	def get_department(self, instance):
		return Department.objects.filter(
			id=Structure.objects.filter(id=instance.reg_structure_id).first().department_id).first().name

	def get_specialization(self, instance):
		return Specialization.objects.filter(
			id=Structure.objects.filter(id=instance.reg_structure_id).first().specialization_id).first().name

