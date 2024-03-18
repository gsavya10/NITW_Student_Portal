from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from registration.models import *
from open_elective.models import *
from results.models import Results
from django.contrib.auth.decorators import login_required
import re
import ast

# Create your views here.
def viewInstructions(request):

    #Modify data to take input of the logged in user and check if allowed or not
    data = {}
    data['registration_number'] = 911680
    data['roll_number'] = 167158

    reg_tuple = Registered.objects.filter(registration_number=data['registration_number'])
    if reg_tuple.count() == 0:
        return render(request, 'open_elective/instructions.djt',
                      {'student': data['registration_number'], 'error': 'User registration data not found.'})

    #check if student is allowed or not. For now, only Semesters, 6 & 7 are allowed.
    student_details = Registered.objects.filter(registration_number=data['registration_number']).order_by('-reg_structure_id')
    if student_details.count() == 0:
        return render(request, 'open_elective/instructions.djt',
                      {'student': data['registration_number'], 'error': 'User registration data not found.'})
    curr_semester = student_details[0].reg_structure.semester
    if curr_semester not in [5, 6]: #Dynamically add support for other semesters by adding 'YOUR_SEMESTER - 1' value in this array
         return render(request, 'open_elective/instructions.djt', {'error': 'You are not allowed! Reason current semester is '+str(curr_semester)})


    #cgpa retrieval
    cgpa = Cgupdate.objects.filter(rollno=data['roll_number'])
    if cgpa.count() == 0:
        cgpa = Results.objects.filter(regno=data['roll_number']).order_by('-reference_id')
    if cgpa.count() == 0:
        return render(request, 'open_elective/instructions.djt', {'student': data['roll_number'], 'error': 'User results data not found.'})
    else:
        cgpa = cgpa[0].cgpa

    #Allotment retrieval
    allotted_elective = StudentElectives.objects.filter(roll=data['roll_number'])
    allotted = 0
    if allotted_elective.count() != 0 and allotted_elective[0].allotted == 1:
        allotted_code = allotted_elective[0].allotted_elective
        course_equivalent = Courses.objects.filter(cid=allotted_code)
        allotted = allotted_code + " - " + course_equivalent[0].name

    return render(request, 'open_elective/instructions.djt', {'regno': data['registration_number'], 'allotted': allotted, 'cgpa': cgpa, 'semester': curr_semester, 'error': 0})


def viewApplications(request):
    session_code = 10  #change this manually for each semester
    ################COPIED FROM ABOVE#############################
    # Modify data to take input of the logged in user and check if allowed or not
    data = {}
    data['registration_number'] = 911680
    data['roll_number'] = 167158

    reg_tuple = Registered.objects.filter(registration_number=data['registration_number'])
    if reg_tuple.count() == 0:
        return render(request, 'open_elective/instructions.djt',
                      {'student': data['registration_number'], 'error': 'User registration data not found.'})

    # check if student is allowed or not. For now, only Semesters, 6 & 7 are allowed.
    student_details = Registered.objects.filter(registration_number=data['registration_number']).order_by(
        '-reg_structure_id')
    if student_details.count() == 0:
        return render(request, 'open_elective/instructions.djt',
                      {'student': data['registration_number'], 'error': 'User registration data not found.'})
    curr_semester = student_details[0].reg_structure.semester
    if curr_semester not in [5, 6]:  # Dynamically add support for other semesters by adding 'YOUR_SEMESTER - 1' value in this array
        return render(request, 'open_elective/instructions.djt',
                      {'error': 'You are not allowed! Reason current semester is ' + str(curr_semester)})

    ############################TILL HERE######################################################

    #Session
    session = Sessions.objects.filter(code=session_code)

    if session.count() == 0:
        return render(request, 'open_elective/instructions.djt',
                      {'error': 'The allotment is yet to be started!'})

    # User's existing selections
    current_selections = StudentElectiveChoices.objects.filter(student_id=data['roll_number']).order_by('priority')
    selections = []
    for options in current_selections:
        course_equivalent = Courses.objects.filter(cid=options.course_id)[0].name
        temp_tuple = {'priority': options.priority, 'name': course_equivalent, 'cid': options.course_id}
        selections.append(temp_tuple)

    return render(request, 'open_elective/preferences.djt', {'selections': selections, 'error': 0})


def storeChoices(request):
    # Modify data to take input of the logged in user
    data = {}
    data['registration_number'] = 911680
    data['roll_number'] = 167158

    # need to store to db
    if request.method == 'POST':
        choices = request.POST['choices']
        # print(choices)
        choicesjson = choices[1:-1]  # Removes the [] brackets
        # print(choicesjson)
        arr = re.findall("\{(.*?)\}", choicesjson)  # Splits on the {} brackets
        # print(arr)
        for choice in arr:
            choicemodified = '{'+choice+'}'  # Adds the {} brackets to make it a JSON object string
            # print(choicemodified)
            choice2 = ast.literal_eval(choicemodified)  # Converts JSON object string to a JSON object
            # print('Priority: '+choice2['priority']+', cid: '+choice2['cid'])
            current_selections = StudentElectiveChoices.objects.filter(student_id=data['roll_number'],
                                                                       course_id=choice2['cid'])[0]
            # print('Existing priority: '+str(current_selections.priority))
            current_selections.priority = int(choice2['priority'])
            current_selections.save()

        return HttpResponseRedirect('')
    else:
        return render(request, 'open_elective/preferences.djt', {'error': 'The request could not be processed!'})
