from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from studentdata.models import StudentData
from .models import Results, Subjects, Info, Session
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
	currUserObj = StudentData.objects.get(userid=request.session['_auth_user_id'])
	currUserRegNo = currUserObj.roll_number # results uses ROLL NUMBER NOT reg no
	currUserResults = Results.objects.filter(regno=currUserRegNo).order_by('-reference_id')
	currUserSubjects = Subjects.objects.none()
	currUserInfo = Info.objects.none()
	resultSessions = Session.objects.none()
	for result in currUserResults:
		ref_id = result.reference_id
		info = Info.objects.filter(reference_id=ref_id)
		# if info[0].publish_status == 0:
		# 	currUserResults = currUserResults.exclude(reference_id=ref_id)
		# 	continue

		session_id = info[0].session_id
		session = Session.objects.filter(id=session_id)
		# if session[0].results_publish==0:
		# 	currUserResults = currUserResults.exclude(reference_id=ref_id)
		# 	continue

		currUserSubjects = currUserSubjects | Subjects.objects.filter(reference_id=ref_id)
		currUserInfo = currUserInfo | info
		resultSessions = resultSessions | session


	currUserSubjects = currUserSubjects.order_by('-reference_id')
	resultSessions = resultSessions.order_by('-id')
	zipped_data = zip(currUserResults, currUserSubjects, currUserInfo, resultSessions)
	return render(request, 'results/main.djt', {'zipped_data': zipped_data})