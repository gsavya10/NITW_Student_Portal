from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from studentdata.models import StudentData
from .models import *
from django.db.models import Sum


from .forms import AddTransactionDetails

# Create your views here.


def index(request):
	data = {'registration_number': 'MC17101'}
	registered = Registered.objects.filter(registration_number=data['registration_number'])
	student_data = StudentData.objects.filter(registration_number=data['registration_number'])
	data['registered'] = []

	for reg in registered:
		section = reg.reg_section
		structure_id = reg.reg_structure_id
		r = {}
		sum =0
		r['section'] = section
		r['courses'] = []
		r['credit'] = []
		# r['specialization'] = m.reg_specialization_name
		q = RegisteredCourses.objects.filter(registered_id=reg.id)
		f = q.first()
		# k = DepartmentSpecialization.objects.filter(specialization_id = f.structure_id)
		# k = k.first()
		# special = .objects.filter(specialization_id = k.specialization_id)
		# special = special.first()
		# r['specialization'] = special.name
		struct = Structure.objects.filter(id = structure_id)
		s = struct.first()
		dept_id = s.department_id
		spec_id = s.specialization_id
		department = Department.objects.filter(id = dept_id)
		department = department.first()
		specialization = Specialization.objects.filter(id = spec_id)
		specialization = specialization.first()


		r['dept_id'] = department.name
		r['spec_id'] = specialization.name
		r['semester'] = s.semester
		for course in q:
			# print(course)
			details = Courses.objects.filter(id=course.course_id)
			for detail in details:
				if(detail.type == 1):
					detail.type = 'THEORY'	
				elif(detail.type == 2):
					detail.type = 'LABORATORY'
				sum = sum + detail.credit

			r['sum'] = sum
			r['courses'].append(details)
		# print(r)
		#for course in q:
			# print(course)
		#	coursedetails = Courses.objects.filter(id=course.course_id)
		#	for coursedetail in coursedetails:
		#		sum += coursedetail.credit
		#
		#	r['credit'].append(coursedetails)
		data['registered'].append(r)


	return render(request, 'registration/home.djt', data)

def getMessInfo(request):
    print("entered")
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = AddTransactionDetails(request.POST)
        # check whether it's valid:
        transaction_id = request.POST['neftPayId']
        
        print(transaction_id)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

    # if a GET (or any other method) we'll create a blank form

    return render(request, 'registration/hostel.djt', {})


