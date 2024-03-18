from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from .models import Feedback, Question, Comment

from registration.models import *

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('value', )
        read_only_fields = ('cfid', 'course_name', 'course_id',
                  'section', 'faculty_name', 'faculty_id', 'session', 'registration_number')

        def create(self, validated_data):
            return Feedback.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.value = validated_data.get('value', instance.value)

            instance.save()

            return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', )
        read_only_fields = ('cfid', 'comment_type', 'course_id',
                  'section', 'faculty_name', 'faculty_id', 'session', 'registration_number')

        def create(self, validated_data):
            return Comment.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.value = validated_data.get('value', instance.value)

            instance.save()

            return instance

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('type_of_course', 'question_for', 'order', 'text')

class CoursesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Courses
        fields = ('id', 'name')

class RegisteredCoursesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = RegisteredCourses
        fields = ('course_id', )
    def to_representation(self, instance):
        serialized_data = super(RegisteredCoursesSerializer, self).to_representation(instance) # original serialized data
        course_id = serialized_data.get('course_id') # get job category id from original serialized data
        course = Courses.objects.using('registration').get(id=course_id) # get the object from db
        serialized_data['course_name'] = course.name # replace id with category name
        return serialized_data # return modified serialized data




