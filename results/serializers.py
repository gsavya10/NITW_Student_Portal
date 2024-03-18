from rest_framework import serializers
from .models import *


class SubjectsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subjects
		fields = '__all__'


class ResultsInfoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Info
		fields = '__all__'


class ResultsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Results
		fields = '__all__'

	info = serializers.SerializerMethodField()
	subjects = serializers.SerializerMethodField()

	def get_info(self, instance):
		return ResultsInfoSerializer(Info.objects.filter(reference_id=instance.reference_id).first()).data

	def get_subjects(self, instance):
		return SubjectsSerializer(Subjects.objects.filter(reference_id=instance.reference_id).first()).data
