from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import serializers
from studentdata.models import Users

import bcrypt
from django.utils.translation import ugettext_lazy as _


class CustomAuthTokenSerializer(AuthTokenSerializer):

	def validate(self, attrs):
		username = attrs.get('username')
		password = attrs.get('password')

		if username and password:
			user = Users.objects.filter(username=username)
			flag = True

			if not user.exists():
				flag = False
			elif not bcrypt.checkpw(password.encode(), user.first().password.encode()):  # check correct credentials provided or not
				flag = False
			if not flag:
				msg = _('Unable to log in with provided credentials.')
				raise serializers.ValidationError(msg, code='authorization')
		else:
			msg = _('Must include "username" and "password".')
			raise serializers.ValidationError(msg, code='authorization')

		attrs['user'] = user.first()
		return attrs


class CustomTokenAuth(ObtainAuthToken):
	serializer_class = CustomAuthTokenSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data, context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		return Response({
			'token': token.key,
			'user_id': user.pk,
			'email': user.email
		})
