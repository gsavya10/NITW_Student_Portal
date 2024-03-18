from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .models import *
from django.db.models import Q
import bcrypt
from django.contrib.auth.decorators import login_required
import random
from django.core.mail import send_mail
import time
import string
import datetime
from django.conf import settings

# Create your views here.

def mLogin(request):
	if request.user.is_authenticated:
		return render(request, 'studentdata/home.djt', {})
	else:
		if request.method == 'POST':
			user = Users.objects.filter(Q(username=request.POST['username']) | Q(email=request.POST['username']))

			if len(user) != 0:
				user = user.get()
			else:
				return render(request, 'studentdata/login.djt', {'error': 1})				

			if not user.active:
				return render(request, 'studentdata/login.djt', {'error': 4})
			elif bcrypt.checkpw(request.POST['passw'].encode('utf-8'), user.password.encode('utf-8')):  # check correct credentials provided or not
				login(request, user)
				return render(request, 'studentdata/home.djt', {})

			else:
				return render(request, 'studentdata/login.djt', {'error': 1})
		else:
			return render(request, 'studentdata/login.djt', {})


def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		repassword = request.POST['repassword']
		regno = request.POST['regno']
		fullname = request.POST['fullname']
		mobile = request.POST['mobileno']

		oldAccount = StudentData.objects.filter(registration_number=regno)

		if Users.objects.filter(username=username).exists():
			return render(request, 'studentdata/login.djt', {'error': 2})
		elif len(oldAccount) != 0 and Users.objects.filter(id=oldAccount[0].userid).exists():
			return render(request, 'studentdata/login.djt', {'error': 2})
		elif repassword != password:
			return render(request, 'studentdata/login.djt', {'error': 3})

		studentUser = Users()

		if len(oldAccount) != 0:
			studentUser.id = oldAccount[0].userid

		studentUser.username = username
		studentUser.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
		studentUser.email = request.POST['email']
		studentUser.first_name = fullname
		studentUser.phone = mobile
		studentUser.active = 0
		studentUser.profile_edited = 0
		studentUser.created_on = int(time.time())
		studentUser.activation_code = "usr" + str(random.randint(10000000000, 99999999999))

		student = StudentData()
		student.name = fullname
		student.roll_number = request.POST['rollno']
		student.registration_number = regno
		student.gender = request.POST['gender']
		student.birthday = request.POST['dob']
		student.mobile = mobile
		student.created_time = datetime.datetime.now()

		subject = "WSDC Student Portal Activation."
		content = "Hi " + fullname + ". Your WSDC Student Portal account has been created.\n"
		content += "Visit " + str(request.META['HTTP_HOST']) + "/activate/" + studentUser.activation_code + "/ to activate your account.\n\n"
		content += "Contact the WSDC Team in case of any problems during signup or activation."

		try:
			send_mail(subject, content, 'abyswp@gmail.com', [studentUser.email], fail_silently=False,)		
		except:
			return render(request, 'studentdata/login.djt', {'error': 7})

		studentUser.save()
		student.userid = studentUser.id

		if len(oldAccount) == 0:
			student.save()

		return render(request, 'studentdata/login.djt', {"success": 1})
	else:
		return render(request, 'studentdata/login.djt', {"error": 99})


@login_required
def editProfile(request):
	student = get_object_or_404(StudentData, userid=request.user.id)

	if request.method == 'GET':

		student = get_object_or_404(StudentData, userid=request.user.id)
		return render(request, 'studentdata/profile.djt', {'student': student})
	elif request.method == 'POST':

		studentUser = get_object_or_404(Users, id=request.user.id)		
		student.name = request.POST['fullname'] 
		student.gender = request.POST['gender']
		student.birthday = request.POST['dob']
		student.nationality = request.POST['nationality']
		student.passport = request.POST['passport']
		student.address = request.POST['paddress']
		studentUser.email = request.POST['email']
		student.mobile = request.POST['mobileno']
		studentUser.mobile = student.mobile
		student.homenumber = request.POST['homephone']
		student.emergency_contact = request.POST['emergencyphone']
		student.guardian1 = request.POST['guardian1name']
		student.relationship1 = request.POST['guardian1rel']
		student.mobile1 = request.POST['guardian1mob']
		student.email1 = request.POST['guardian1mail']
		student.guardian2 = request.POST['guardian2name']
		student.relationship2 = request.POST['guardian2rel']
		student.mobile2 = request.POST['guardian2mob']
		student.email2 = request.POST['guardian2mail']
		student.joining_year = request.POST['joinyr']
		student.branch = request.POST['branch']
		student.course = request.POST['course']
		student.current_section = request.POST['section']
		student.sbh_account = request.POST['sbiacc']
		student.adhaar = request.POST['AadhaarIsSafe']
		student.bloodgroup = request.POST['bloodgrp']
		student.mac = request.POST['laptopmac']

		student.save()
		studentUser.save()

		return render(request, 'studentdata/profile.djt', {'saved': 1, 'student': student})


def activateUser(request, arg):
	student = Users.objects.filter(activation_code=arg)

	if len(student) == 0:
		return render(request, 'studentdata/activate.djt', {'error': 1})

	for item in student:
		item.active = 1
		item.save()

	return render(request, 'studentdata/activate.djt', {'error': 0})


def forgotPassword(request):
	if request.method == 'POST':
		student = Users.objects.filter(username=request.POST['usrnm'])

		if len(student) == 0 or not StudentData.objects.filter(registration_number=request.POST['regnum'], userid=student[0].id).exists():
			return render(request, 'studentdata/login.djt', {'error': 5})
		else:
			student = student[0]

		rand_pass = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(20)])

		subject = "WSDC Password Reset."
		content = "Hi " + student.username + ". Your temporary password is: " + str(rand_pass) + "\n"
		content += "Use this to login, but you should change this password after logging in to your account."

		try:
			send_mail(subject, content, 'abyswp@gmail.com', [student.email], fail_silently=False,)		
		except:
			return render(request, 'studentdata/login.djt', {'error': 7})			
		
		student.password = bcrypt.hashpw(rand_pass.encode('utf-8'), bcrypt.gensalt()).decode()
		student.save()

		return render(request, 'studentdata/login.djt', {'success': 2})	


@login_required
def changePassword(request):
	if request.method == 'GET':
		return render(request, 'studentdata/changepassword.djt', {})
	elif request.method == 'POST':
		oldpass = request.POST['cpass']
		newpass = request.POST['npass']
		renewpass = request.POST['renpass']

		if bcrypt.checkpw(oldpass.encode('utf-8'), request.user.password.encode('utf-8')) and newpass == renewpass:
			studentUser = get_object_or_404(Users, id=request.user.id)

			studentUser.password = bcrypt.hashpw(newpass.encode('utf-8'), bcrypt.gensalt()).decode()
			studentUser.save()

			return render(request, 'studentdata/changepassword.djt', {'saved': 1})
		else:
			return render(request, 'studentdata/changepassword.djt', {'saved': 2})


def mLogout(request):
	logout(request)
	return redirect('/')

