import django
from feedback.models import Question

LAB = 'L'
THEORY = 'T'
COURSE = 'C'
FACULTY = 'F'

TYPE_OF_COURSE_CHOICES = (
    (LAB, 'Lab'),
    (THEORY, 'Theory'),
)
QUESTION_FOR_CHOICES = (
    (COURSE, 'Course'),
    (FACULTY, 'Faculty'),
)
# Format for creating object of Question -  Question.objects.create(type_of_course = LAB, question_for = COURSE, order = , text)

    # //error messages
    # $lang['ErrorSubmit']  = "Opps! Some error occured try again later.";
    # $lang['ErrorComplete'] = "All the Questions are mandatory.";
    # $lang['Success'] = "Feedback Succesfully submitted.";

def run():
    # Laboratory Questions for the Course
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 1, text = "Dissemination of the course outcomes, description of the experiments and lab manuals")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 2, text = "Accomplishment of the attainment of specified course outcomes")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 3, text = "Usefulness of the laboratory experiments to achieve the defined course outcomes")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 4, text = "Relevance of the experiments to the present and futuristic industry requirements")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 5, text = "Usefulness of the laboratory course to improve the understanding of concepts and principles")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 6, text = "Relevance of the experimental setups for proper understanding of major field of study")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 7, text = "Scope for independent learning as well as work in teams")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 8, text = "Scope for effective report writing following ethical principles")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 9, text = "Scope for analysis and interpretation of experimental data to draw valid conclusions")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 10, text = "Support provided by the faculty/technical-staff/research scholars")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 11, text = "Effective collaboration between the laboratory experiments and the allied theory course")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 12, text = "The quality and quantity of experimental setups in the laboratory")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 13, text = "Effective learning vis-a-vis the team size to conduct experiments")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 14, text = "Emphasis on personal and equipment safety")
    Question.objects.create(type_of_course = LAB, question_for = COURSE, order = 15, text = "Overall rating of the laboratory course")

    # Laboratory Questions for the Faculty
    Question.objects.create(type_of_course = LAB, question_for = FACULTY, order = 1, text = "Effective utilization of laboratory time and punctuality")
    Question.objects.create(type_of_course = LAB, question_for = FACULTY, order = 2, text = "Effective organization of the laboratory experiments to meet the desired course outcomes")
    Question.objects.create(type_of_course = LAB, question_for = FACULTY, order = 3, text = "Effectiveness of oral and experimental testing in the laboratory")
    Question.objects.create(type_of_course = LAB, question_for = FACULTY, order = 4, text = "Guidance provided during experimentation")
    Question.objects.create(type_of_course = LAB, question_for = FACULTY, order = 5, text = "Command on the experimental setup and designed learning")
    Question.objects.create(type_of_course = LAB, question_for = FACULTY, order = 6, text = "Help provided to improve the experimental skills")
    Question.objects.create(type_of_course = LAB, question_for = FACULTY, order = 7, text = "Promotion of ethical and social responsibility among students")
    Question.objects.create(type_of_course = LAB, question_for = FACULTY, order = 8, text = "Highlighting the relevant industrial practices")
    Question.objects.create(type_of_course = LAB, question_for = FACULTY, order = 9, text = "Monitoring of the faculty for effective learning")
    Question.objects.create(type_of_course = LAB, question_for = FACULTY, order = 10, text = "Fair & impartial grading in the laboratory")
    Question.objects.create(type_of_course = LAB, question_for = FACULTY, order = 11, text = "Effectiveness of the presence of the faculty in the laboratory")
    Question.objects.create(type_of_course = LAB, question_for = FACULTY, order = 12, text = "Overall effectiveness of the faculty")

    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 1, text = "Dissemination of the course outcomes, lecture plan and relevant course materials")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 2, text = "Accomplishment of the attainment of specified course outcomes")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 3, text = "Adequacy of reading material to meet the specified course outcomes")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 4, text = "Usefulness of the course content to achieve the defined course outcomes")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 5, text = "Relevance of the course to the present and futuristic industry requirements")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 6, text = "Effective relationship between class room sessions and reading material")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 7, text = "Usefulness of the course to improve the understanding of concepts and principles")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 8, text = "Usefulness of the course to identify, formulate and analyze complex situations")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 9, text = "Effectiveness of the course in improving critical and independent thinking")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 10, text = "Essential to attend classes for proper understanding of the subject")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 11, text = "Relevance of the course content to the major field of study")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 12, text = "Impact of the examinations for improved learning")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 13, text = "Scope for independent and life-long learning")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 14, text = "Scope for the use of modern / IT tools and techniques for improved learning")
    Question.objects.create(type_of_course = THEORY, question_for = COURSE, order = 15, text = "Overall rating of the course.")

    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 1, text = "Effective use of blackboard / other visual aids")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 2, text = "Utilization of modern/IT tools relevant for effective understanding")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 3, text = "Punctuality and effective utilization of class time")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 4, text = "Willingness to meet the students outside the class hours")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 5, text = "Effective organization and delivery of the course content as per the teaching plan.")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 6, text = "Academic preparedness of the faculty for each lecture")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 7, text = "Effectiveness of the questions to test the attainment of specified course outcomes")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 8, text = "Fair & impartial evaluation of answer scripts")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 9, text = "Command on the course")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 10, text = "Coherent and effective speaking ability")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 11, text = "Ability of the faculty in providing answers/references to questions and discussions")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 12, text = "Encouragement for questions and discussions from students in the class")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 13, text = "Effective and useful feedback on the performance of students in the tests")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 14, text = "Help provided to improve the problem solving skills")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 15, text = "Promotion of ethical and social responsibility among students")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 16, text = "Highlighting the relevant industrial practices during course delivery")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 17, text = "Created interest in the subject by relating it to other appropriate courses")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 18, text = "Sensitivity to the student’s academic needs")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 19, text = "Effective and useful delivery of contents beyond the scope of the curriculum")
    Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = 20, text = "Overall effectiveness of the faculty.")

    print("Questions added \n")