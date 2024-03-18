from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from registration.models import *
from studentdata.models import *
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def viewAttendance(request):
	student = get_object_or_404(StudentData, userid=request.user.id)
	
	reg_tuple = Registered.objects.filter(registration_number=student.registration_number).order_by('-id') # This one
	if reg_tuple.count() == 0:
		return render(request, 'attendance/viewAttendance.djt', {'student': student, 'error': 'Registration data not found.'})
	else:
		reg_tuple = reg_tuple[0]

	registered_courses = RegisteredCourses.objects.filter(registered_id=reg_tuple.id, mode=1) # This one

	if registered_courses.count() == 0:
		return render(request, 'attendance/viewAttendance.djt', {'student': student, 'error': 'No registered courses.'})			

	current_date = datetime.date.today()
	start_date = datetime.date(current_date.year, 12, 1) if current_date.month in (12, 1, 2, 3, 4, 5, 6) else datetime.date(current_date.year, 7, 1)

	if current_date.month in (1, 2, 3, 4, 5, 6):
		start_date = datetime.date(current_date.year - 1, 12, 1)

	courses = {}			
	for reg_course in registered_courses:
		courses[reg_course] = AttendanceDates.objects.filter(course_id=reg_course.course_id, section=reg_tuple.reg_section, date__gte=start_date).values_list('id', flat=True)

	attendance = []
	for course, classes in courses.items():
		count = len(AttendanceRecord.objects.filter(id__in=classes, rollno=student.roll_number))

		data = {'courseid': course.course_id, 'name': Courses.objects.filter(id=course.course_id).values_list('name', flat=True)[0], 'mode': course.mode, 'attended': count, 'total': len(classes), 'percent': round(float(100*count/len(classes)), 2) if len(classes) != 0 else 'NA', 'backlog': course.backlog} # This one
		attendance.append(data)

	if student.joining_year == '' or int(student.joining_year) > 2014:
		limit = 80
	else:
		limit = 75

	return render(request, 'attendance/viewAttendance.djt', {'student': student, 'attendance': attendance, 'limit': limit, 'error': 0})		
