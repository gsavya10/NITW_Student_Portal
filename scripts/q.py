for i in range(1,21):
    print('Question.objects.create(type_of_course = THEORY, question_for = FACULTY, order = ' + str(i) + ', text = "")')