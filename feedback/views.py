from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from registration.models import RegisteredCourses, Registered, RegularCourses, Courses, CourseFacultyAllotted
from studentdata.models import *
from facultydata.models import *
from .models import *
from datetime import datetime, date, time
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

LAB = 'L'
THEORY = 'T'
COURSE = 'C'
FACULTY = 'F'

FEEDBACK_DEADLINE = datetime.combine(date(2019, 4, 20), time(23, 59, 59))

CURRENT_REGISTRATION_SESSION = 12

FEEDBACK_OPEN = False


def user_is_signed_in(request):
    return request.user.is_authenticated


def user_profile_edited(request):
    return True


@login_required(login_url='/')
def feedback_home(request):

    userid = request.user.id

    #Check if the student is signed in
    if user_is_signed_in(request):

        #Check if the student has edited the profile
        if user_profile_edited(request):

            #Get the student's details
            student = get_object_or_404(StudentData, userid=userid)

            #If the feedback is open
            if FEEDBACK_OPEN == True:
                #Get the student's registration details
                try:
                    registration_tuple = Registered.objects.get(registration_number=student.registration_number, reg_structure__session_id = CURRENT_REGISTRATION_SESSION)
                except Registered.DoesNotExist:
                    message = 'Since you only have subjects falling under categories "COMPREHENSIVE VIVA VOCE" , "DISSERTATION" , "PROJECT WORK" and no theory/lab subjects, filling feedback is not necessary.'
                    response = {
                        'student': student,
                        'message': message
                        }
                    return render(request, 'feedback/registered_courses.html', response)

                #Get the registered courses for current semester
                registered_courses = RegisteredCourses.objects.filter(registered_id=registration_tuple.id)
                batch_index = registered_courses[0].batch
                structure_id = registered_courses[0].structure_id
                # regular_courses = RegularCourses.objects.filter(structure_id = structure_id)
                for registered_course in registered_courses:
                    try:
                        regular_course = RegularCourses.objects.get(structure_id = structure_id, course_id = registered_course.course.id)
                        cfa = CourseFacultyAllotted.objects.get(regular_course_id = regular_course.id, section = student.current_section, batch_index = batch_index) 
                        try: 
                            faculty = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = cfa.faculty_id)
                            registered_course.faculty_name = faculty.name
                        except:
                            #No faculty has been allotted 
                            print(cfa)
                            # Civil Engineering
                            if registered_course.structure.department_id == 1:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16193).name
                            # Electrical Engineering
                            elif registered_course.structure.department_id == 2:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16443).name
                            # Mechanical Engineering
                            elif registered_course.structure.department_id == 3:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16257).name
                            # Electronics & Communication Engineering
                            elif registered_course.structure.department_id == 4:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16455).name
                            # Metallurgical & Materials Engineering
                            elif registered_course.structure.department_id == 5:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16485).name
                            # Chemical Engineering
                            elif registered_course.structure.department_id == 6:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16446).name
                            # Computer Science & Engineering
                            elif registered_course.structure.department_id == 7:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16447).name
                            # Biotechnology
                            elif registered_course.structure.department_id == 8:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16693).name
                            # Physics
                            elif registered_course.structure.department_id == 9:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16449).name
                            # Chemistry
                            elif registered_course.structure.department_id == 10:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16380).name
                            # Mathematics
                            elif registered_course.structure.department_id == 11:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16451).name
                            # Humanities & Social Science
                            elif registered_course.structure.department_id == 12:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16610).name
                            # Physical Education
                            elif registered_course.structure.department_id == 13:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16495).name
                            # School of Management
                            elif registered_course.structure.department_id == 14:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16453).name
                            # Testing Account, WSDC
                            elif registered_course.structure.department_id == 15:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16257).name
                            # No Branch
                            elif registered_course.structure.department_id == 21:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16613).name
                        try:
                            feedback = Feedback.objects.get(registration_number = student.registration_number, cfid = cfa.id)
                            registered_course.feedback_status = 1
                        except Feedback.DoesNotExist:
                            print("Feedback object doesn't exist", cfa)
                            registered_course.feedback_status = 0 
                    except RegularCourses.DoesNotExist:
                        print(structure_id, registered_course.course.id)
                        print(registered_course.structure)
                            
                #There are no registered courses
                if registered_courses.count() == 0:
                    error = 'No registered courses.'
                    response = {
                        'student': student,  
                        'error': error
                    }
                    return render(request, 'feedback/registered_courses.html', response)
                
                #Get details of whether the feedback has already been filled
                
                filled_feedback = FilledFeedback.objects.using('feedback_db').filter(registration_number=student.registration_number, session__registration_session=CURRENT_REGISTRATION_SESSION)
                message = ''

                #Feedback has not been filled yet
                if filled_feedback.count() == 0:
                    message = 'Feedback is not yet filled completely. Please completely fill the feedback before ' + FEEDBACK_DEADLINE.strftime('%H') + ':' + FEEDBACK_DEADLINE.strftime('%M') + ':' + FEEDBACK_DEADLINE.strftime('%S') + ' on ' + FEEDBACK_DEADLINE.strftime('%A') + ', ' + FEEDBACK_DEADLINE.strftime('%w') + ' ' + FEEDBACK_DEADLINE.strftime('%B') + ' ' + FEEDBACK_DEADLINE.strftime('%Y') + ' to avoid Rs. 500 fine.'
                    response = {
                        'student': student,
                        'message': message,  
                        'registered_courses': registered_courses,
                        'negative_message': True,
                        'can_fill_feedback': True,
                    }
                    return render(request, 'feedback/registered_courses.html', response)
                else:
                    message = 'Congratulations! You have successfully filled the Feedback. Your reference number is: ' + FEEDBACK_DEADLINE.strftime('%Y') + str(filled_feedback[0].id) + '. Keep this with you for further communication.'
                    response = {
                        'student': student,
                        'message': message,  
                        'registered_courses': registered_courses,
                        'positive_message': True,
                        'can_fill_feedback': False,
                    }
                    return render(request, 'feedback/registered_courses.html', response)
            #If feedback is not open
            elif FEEDBACK_OPEN == False:
                #Get last semester's registration details
                try:
                    registration_tuple = Registered.objects.get(registration_number=student.registration_number, reg_structure__session_id = CURRENT_REGISTRATION_SESSION - 1)
                except Registered.DoesNotExist:
                    message = 'Since you only have subjects falling under categories "COMPREHENSIVE VIVA VOCE" , "DISSERTATION" , "PROJECT WORK" and no theory/lab subjects, filling feedback is not necessary.'
                    response = {
                        'student': student,
                        'message': message
                        }
                    return render(request, 'feedback/registered_courses.html', response)

                #Get last semester's registered courses
                registered_courses = RegisteredCourses.objects.filter(registered_id=registration_tuple.id)
                structure_id = registered_courses[0].structure_id
                batch_index = registered_courses[0].batch
                regular_courses = RegularCourses.objects.filter(structure_id = structure_id)
                for registered_course in registered_courses:
                    try:
                        regular_course = RegularCourses.objects.get(structure_id = structure_id, course_id = registered_course.course.id)
                        cfa = CourseFacultyAllotted.objects.get(regular_course_id = regular_course.id, section = student.current_section, batch_index = batch_index) 
                        try: 
                            faculty = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = cfa.faculty_id)
                            registered_course.faculty_name = faculty.name
                        except:
                            #No faculty has been allotted 
                            print(cfa)
                            # Civil Engineering
                            if registered_course.structure.department_id == 1:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16193).name
                            # Electrical Engineering
                            elif registered_course.structure.department_id == 2:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16443).name
                            # Mechanical Engineering
                            elif registered_course.structure.department_id == 3:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16257).name
                            # Electronics & Communication Engineering
                            elif registered_course.structure.department_id == 4:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16455).name
                            # Metallurgical & Materials Engineering
                            elif registered_course.structure.department_id == 5:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16485).name
                            # Chemical Engineering
                            elif registered_course.structure.department_id == 6:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16446).name
                            # Computer Science & Engineering
                            elif registered_course.structure.department_id == 7:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16447).name
                            # Biotechnology
                            elif registered_course.structure.department_id == 8:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16693).name
                            # Physics
                            elif registered_course.structure.department_id == 9:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16449).name
                            # Chemistry
                            elif registered_course.structure.department_id == 10:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16380).name
                            # Mathematics
                            elif registered_course.structure.department_id == 11:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16451).name
                            # Humanities & Social Science
                            elif registered_course.structure.department_id == 12:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16610).name
                            # Physical Education
                            elif registered_course.structure.department_id == 13:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16495).name
                            # School of Management
                            elif registered_course.structure.department_id == 14:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16453).name
                            # Testing Account, WSDC
                            elif registered_course.structure.department_id == 15:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16257).name
                            # No Branch
                            elif registered_course.structure.department_id == 21:
                                registered_course.faculty_name = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = 16613).name
                        try:
                            feedback = Feedback.objects.get(registration_number = student.registration_number, cfid = cfa.id)
                            registered_course.feedback_status = 1
                        except Feedback.DoesNotExist:
                            print("Feedback object doesn't exist", cfa)
                            registered_course.feedback_status = 0 
                    except RegularCourses.DoesNotExist:
                        print(structure_id, registered_course.course.id)
                        print(registered_course.structure)

                #If there are no registered courses
                if registered_courses.count() == 0:
                    message = 'No registered courses.'
                    response = {
                        'student': student,  
                        'message': message,
                        'negative_message': True
                    }
                    return render(request, 'feedback/registered_courses.html', response)
                
                #Get details of whether the feedback was filled when it was open
                filled_feedback = FilledFeedback.objects.using('feedback_db').filter(registration_number=student.registration_number, session__registration_session=CURRENT_REGISTRATION_SESSION - 1)

                message = ''

                
                #If feedback was not filled while it was open
                if filled_feedback.count() == 0:

                    #If permission to still fill feedback is given
                    try:
                        Allow.objects.using('feedback_db').get(registration_number=student.registration_number, session__registration_session=CURRENT_REGISTRATION_SESSION - 1)
                        message = 'Feedback is not yet filled completely. Please completely fill the feedback.'
                        response = {
                                'student': student,
                                'message': message,  
                                'registered_courses': registered_courses,
                                'negative_message': True,
                                'can_fill_feedback': True,
                            }
                        return render(request, 'feedback/registered_courses.html', response)

                    #If permission to fill feedback after closing is not given
                    except:
                        message = "You haven't filled the feedback. You will need to pay Rs.500 fine to unlock this feedback. Your results will be published only after you fill the feedback. Contact WSDC FB page with your reference number in case you did fill the feedback."
                        response = {
                            'student': student,
                            'message': message,  
                            'registered_courses': registered_courses,
                            'negative_message': True,
                            'can_fill_feedback': False,
                        }
                        return render(request, 'feedback/registered_courses.html', response)

                #If feedback was filled while it was open
                else:
                    message = 'Congratulations! You have successfully filled the Feedback. Your reference number is: ' + FEEDBACK_DEADLINE.strftime('%Y') + str(filled_feedback[0].id) + '. Keep this with you for further communication.'
                    response = {
                        'student': student,
                        'message': message,  
                        'registered_courses': registered_courses,
                        'positive_message': True,
                        'can_fill_feedback': False,
                    }
                    return render(request, 'feedback/registered_courses.html', response)
            
        else:
            #Change this to redirect to edit profile
            return render(request, 'studentdata/login.djt', {}) 
    else:
        return render(request, 'studentdata/login.djt', {})


@login_required(login_url='/')
def fill_feedback(request, courseID):

    userid = request.user.id
    if user_is_signed_in(request):

        if user_profile_edited(request):

            student = get_object_or_404(StudentData, userid=userid)

            try:
                if FEEDBACK_OPEN == True:
                    registration_tuple = Registered.objects.get(registration_number=student.registration_number, reg_structure__session_id = CURRENT_REGISTRATION_SESSION)
                else:
                    registration_tuple = Registered.objects.get(registration_number=student.registration_number, reg_structure__session_id = CURRENT_REGISTRATION_SESSION - 1)
            except Registered.DoesNotExist:
                return feedback_home(request)
            
            registered_course = RegisteredCourses.objects.get(registered_id=registration_tuple.id, course__id = courseID)
            batch_index = registered_course.batch
            structure_id = registered_course.structure_id
            regular_course = RegularCourses.objects.get(structure_id = structure_id, course_id = courseID)
            cfa = CourseFacultyAllotted.objects.get(regular_course_id = regular_course.id, section = student.current_section, batch_index = batch_index)  
            faculty = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = cfa.faculty_id)
            registered_course.faculty_name = faculty.name
            
            if registered_course.course.type == 1:
                theory_course_questions = (Question.objects.filter(type_of_course=THEORY, question_for=COURSE)).order_by('order')
                theory_faculty_questions = (Question.objects.filter(type_of_course=THEORY, question_for=FACULTY)).order_by('order')

                response = {
                    'course_questions': theory_course_questions,
                    'faculty_questions': theory_faculty_questions,
                    'registered_course': registered_course,
                    'course_type': THEORY
                }

                return render(request, 'feedback/feedback_form.html', response)
            if registered_course.course.type == 2:

                lab_course_questions = (Question.objects.filter(type_of_course=LAB, question_for=COURSE)).order_by('order')
                lab_faculty_questions = (Question.objects.filter(type_of_course=LAB, question_for=FACULTY)).order_by('order')

                response = {
                    'course_questions':lab_course_questions,
                    'faculty_questions':lab_faculty_questions,
                    'registered_course': registered_course,
                    'course_type':LAB
                }

                return render(request, 'feedback/feedback_form.html', response)
        else:
            #Change this to redirect to edit profile
            return render(request, 'studentdata/login.djt', {}) 
    else:
        return render(request, 'studentdata/login.djt', {})


@login_required(login_url='/')
def submit_feedback(request, courseID):
    print("Submitting feedback")
    if request.method == 'POST':
        if user_is_signed_in(request):

            if user_profile_edited(request):
                student = get_object_or_404(StudentData, userid=request.user.id)

                course = Courses.objects.get(id=courseID)
                feedback = ''
                print(request.POST)
                if course.type == 1:
                    for i in range(1, 16):
                        feedback += request.POST.get('courseFeedback' + str(i))

                    for i in range(1, 21):
                        feedback += request.POST.get('facultyFeedback' + str(i))

                elif course.type == 2:
                    for i in range(1, 16):
                        feedback += request.POST.get('courseFeedback' + str(i))

                    for i in range(1, 13):
                        feedback += request.POST.get('facultyFeedback' + str(i))
                if FEEDBACK_OPEN == True:
                    from .models import Session as FeedbackSession
                    session = FeedbackSession.objects.using('feedback_db').get(registration_session = CURRENT_REGISTRATION_SESSION)
                    try:
                        registration_tuple = Registered.objects.get(registration_number=student.registration_number, reg_structure__session_id = CURRENT_REGISTRATION_SESSION)
                    except Registered.DoesNotExist:
                        return feedback_home(request)
                    registered_course = RegisteredCourses.objects.get(registered_id=registration_tuple.id, course__id = courseID)
                    batch_index = registered_course.batch
                    structure_id = registered_course.structure_id
                    regular_course = RegularCourses.objects.get(structure_id = structure_id, course_id = courseID)
                    cfa = CourseFacultyAllotted.objects.get(regular_course_id = regular_course.id, section = student.current_section, batch_index = batch_index)  
                    faculty = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = cfa.faculty_id)
                    registered_course.faculty_name = faculty.name
                
                    f = Feedback.objects.create(cfid = cfa.id, value = feedback, session = session, course_id = regular_course.course_id, course_name = registered_course.course.name, registration_number = student.registration_number, section = student.current_section, faculty_name = faculty.name, faculty_id = faculty.facultyid)
                    if len(request.POST['courseComment1']) > 0:
                        Comment.objects.create(cfid = cfa.id, comment_type = 1, comment = request.POST['courseComment1'], registration_number = student.registration_number, course_id = regular_course.course_id, course_name = registered_course.course.name, section = student.current_section, faculty_name = faculty.name, faculty_id = faculty.facultyid, session = session)
                    if len(request.POST['courseComment2']) > 0:
                        Comment.objects.create(cfid = cfa.id, comment_type = 2, comment = request.POST['courseComment2'], registration_number = student.registration_number, course_id = regular_course.course_id, course_name = registered_course.course.name, section = student.current_section, faculty_name = faculty.name, faculty_id = faculty.facultyid, session = session)
                    if len(request.POST['facultyComment1']) > 0:
                        Comment.objects.create(cfid = cfa.id, comment_type = 3, comment = request.POST['facultyComment1'], registration_number = student.registration_number, course_id = regular_course.course_id, course_name = registered_course.course.name, section = student.current_section, faculty_name = faculty.name, faculty_id = faculty.facultyid, session = session)
                    if len(request.POST['facultyComment2']) > 0:
                        Comment.objects.create(cfid = cfa.id, comment_type = 4, comment = request.POST['facultyComment2'], registration_number = student.registration_number, course_id = regular_course.course_id, course_name = registered_course.course.name, section = student.current_section, faculty_name = faculty.name, faculty_id = faculty.facultyid, session = session)
                    
                    feedbacks = Feedback.objects.filter(session = session, registration_number = student.registration_number)
                    registered_courses = RegisteredCourses.objects.filter(registered_id=registration_tuple.id)

                    feedbacks = Feedback.objects.filter(session = session, registration_number = student.registration_number)
                    registered_courses = RegisteredCourses.objects.filter(registered_id=registration_tuple.id)
                    if (feedbacks.count() == registered_courses.count()):
                        FilledFeedback.objects.create(registration_number = student.registration_number, session = session)
                    return feedback_home(request)
                    
                elif FEEDBACK_OPEN == False:
                    from .models import Session as FeedbackSession
                    previous_session = FeedbackSession.objects.using('feedback_db').get(registration_session = CURRENT_REGISTRATION_SESSION - 1)
                    try:
                        registration_tuple = Registered.objects.get(registration_number=student.registration_number, reg_structure__session_id = CURRENT_REGISTRATION_SESSION - 1)
                    except Registered.DoesNotExist:
                        return feedback_home(request)
                    registered_course = RegisteredCourses.objects.get(registered_id=registration_tuple.id, course__id = courseID)
                    batch_index = registered_course.batch
                    structure_id = registered_course.structure_id
                    regular_course = RegularCourses.objects.get(structure_id = structure_id, course_id = courseID)
                    cfa = CourseFacultyAllotted.objects.get(regular_course_id = regular_course.id, section = student.current_section, batch_index = batch_index)  
                    faculty = FacultyCurrentData.objects.using('faculty_profile').get(facultyid = cfa.faculty_id)
                    registered_course.faculty_name = faculty.name
                
                    f = Feedback.objects.create(cfid = cfa.id, value = feedback, session = previous_session, course_id = regular_course.course_id, course_name = registered_course.course.name, registration_number = student.registration_number, section = student.current_section, faculty_name = faculty.name, faculty_id = faculty.facultyid)
                    if len(request.POST['courseComment1']) > 0:
                        Comment.objects.create(cfid = cfa.id, comment_type = 1, comment = request.POST['courseComment1'], registration_number = student.registration_number, course_id = regular_course.course_id, course_name = registered_course.course.name, section = student.current_section, faculty_name = faculty.name, faculty_id = faculty.facultyid, session = previous_session)
                    if len(request.POST['courseComment2']) > 0:
                        Comment.objects.create(cfid = cfa.id, comment_type = 2, comment = request.POST['courseComment2'], registration_number = student.registration_number, course_id = regular_course.course_id, course_name = registered_course.course.name, section = student.current_section, faculty_name = faculty.name, faculty_id = faculty.facultyid, session = previous_session)
                    if len(request.POST['facultyComment1']) > 0:
                        Comment.objects.create(cfid = cfa.id, comment_type = 3, comment = request.POST['facultyComment1'], registration_number = student.registration_number, course_id = regular_course.course_id, course_name = registered_course.course.name, section = student.current_section, faculty_name = faculty.name, faculty_id = faculty.facultyid, session = previous_session)
                    if len(request.POST['facultyComment2']) > 0:
                        Comment.objects.create(cfid = cfa.id, comment_type = 4, comment = request.POST['facultyComment2'], registration_number = student.registration_number, course_id = regular_course.course_id, course_name = registered_course.course.name, section = student.current_section, faculty_name = faculty.name, faculty_id = faculty.facultyid, session = previous_session)
                    
                    feedbacks = Feedback.objects.filter(session = previous_session, registration_number = student.registration_number)
                    registered_courses = RegisteredCourses.objects.filter(registered_id=registration_tuple.id)

                    if FEEDBACK_OPEN == True:
                        feedbacks = Feedback.objects.filter(session = previous_session, registration_number = student.registration_number)
                        registered_courses = RegisteredCourses.objects.filter(registered_id=registration_tuple.id)
                    if (feedbacks.count() == registered_courses.count()):
                        FilledFeedback.objects.create(registration_number = student.registration_number, session = previous_session)
                    return feedback_home(request)
            else:
                #Change this to redirect to edit profile
                return render(request, 'studentdata/login.djt', {}) 
        else:
            return render(request, 'studentdata/login.djt', {})
    else:
        return feedback_home(request)


class FeedbackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows feedback to be viewed or edited.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class RegisteredCoursesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows feedback to be viewed or edited.
    """
    queryset = RegisteredCourses.objects.filter(registered_id=(Registered.objects.filter(registration_number=(get_object_or_404(StudentData, userid=7600)).registration_number)).order_by('-id')[0])
    serializer_class = RegisteredCoursesSerializer

@api_view(['GET'])
def get_questions(request, courseID):
    if request.method == 'GET':
        course = Courses.objects.get(id = courseID)
        print(course.name)
        questions = []
        if course.type == 1:
            questions = Question.objects.filter(type_of_course = THEORY)
        elif course.type == 2:
            questions = Question.objects.filter(type_of_course = LAB)
        serializer = QuestionSerializer(questions, many=True)
        print(serializer.data)
        return Response(serializer.data)