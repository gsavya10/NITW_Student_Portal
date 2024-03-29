"""
Django settings for StudentPortal project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-%hicap2+-&bqwfprwnobn4fmvokt33ki9w=)f%shtpt6_azgb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django_extensions',
	'studentdata',
	'results',
	'attendance',
	'registration',
	'facultydata',
	'feedback',
	'open_elective',
	'rest_framework',
	'rest_framework.authtoken',
	# 'bcrypt',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'StudentPortal.urls'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'abyswp@gmail.com'
EMAIL_HOST_PASSWORD = 'mahbusiness'
EMAIL_PORT = 587

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates'),],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'StudentPortal.wsgi.application'

REST_FRAMEWORK = {
	# Use Django's standard `django.contrib.auth` permissions,
	# or allow read-only access for unauthenticated users.
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
	],
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.TokenAuthentication',
		'rest_framework.authentication.SessionAuthentication',
	),
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
	'PAGE_SIZE': 100
}


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
	'default': {
		'NAME': 'wsdc_student',
		'HOST': '127.0.0.1',
		'ENGINE': 'django.db.backends.mysql',
		'USER': 'django',
		'PASSWORD': 'django-user-password',
	},

	'feedback_db': {
		'NAME': 'feedback',
		'HOST': '127.0.0.1',
		'ENGINE': 'django.db.backends.mysql',
		'USER': 'django',
		'PASSWORD': 'django-user-password',
	},

	'faculty_profile': {
		'NAME': 'faculty_profile',
		'HOST': '127.0.0.1',
		'ENGINE': 'django.db.backends.mysql',
		'USER': 'django',
		'PASSWORD': 'django-user-password',
	},

	'wsdc_results': {
		'NAME': 'wsdc_results',
		'HOST': '127.0.0.1',
		'ENGINE': 'django.db.backends.mysql',
		'USER': 'django',
		'PASSWORD': 'django-user-password',
	},
	'wsdc_electives': {
		'NAME': 'wsdc_electives',
		'HOST': '127.0.0.1',
		'ENGINE': 'django.db.backends.mysql',
		'USER': 'django',
		'PASSWORD': 'django-user-password',
	},
	'registration': {
		'NAME': 'registration',
		'HOST': '127.0.0.1',
		'ENGINE': 'django.db.backends.mysql',
		'USER': 'django',
		'PASSWORD': 'django-user-password',
	},
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'studentdata.Users'

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

PASSWORD_HASHERS = (
	'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
	'django.contrib.auth.hashers.BCryptPasswordHasher',
	'django.contrib.auth.hashers.PBKDF2PasswordHasher',
	'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
	'django.contrib.auth.hashers.SHA1PasswordHasher',
	'django.contrib.auth.hashers.MD5PasswordHasher',
	'django.contrib.auth.hashers.CryptPasswordHasher',
)


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = ('./static',)


DATABASE_ROUTERS = ['feedback.models.FeedbackRouter']
