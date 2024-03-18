from django.db import models
from django.utils import timezone

    
class FeedbackRouter:
    """
    A router to control all database operations on models in the
    feedback application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read feedback models go to auth_db.
        """
        if model._meta.app_label == 'feedback':
            return 'feedback_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == 'feedback':
            return 'feedback_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the feedback app is involved.
        """
        if obj1._meta.app_label == 'feedback' or \
           obj2._meta.app_label == 'feedback':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label == 'feedback':
            return db == 'feedback_db'
        return None

class Session(models.Model):
    name = models.CharField(max_length=30)
    registration_session = models.IntegerField() 

    class Meta:
        db_table = 'session'

class AllowExit(models.Model):
    registration_number = models.CharField(max_length=16)
    reason = models.CharField(max_length=256)
    timestamp = models.DateTimeField(default=timezone.now)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        db_table = 'allow_exit'
        unique_together = (("registration_number", "session"),)

class Allow(models.Model):
    registration_number = models.CharField(max_length=16)
    reason = models.CharField(max_length=500, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        db_table = 'allow'

    
class Feedback(models.Model):
    cfid = models.IntegerField(null=True, blank=True)
    value = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=16)
    course_name = models.CharField(max_length=75)
    course_id = models.CharField(max_length=16)
    section = models.CharField(max_length=2)
    faculty_name = models.CharField(max_length=50)
    faculty_id = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        db_table = 'feedback'

class Comment(models.Model):
    cfid = models.IntegerField(null=True, blank=True)
    COMMENT_TYPE_CHOICES = (
        (1, 'The main strengths of this course are:'),
        (2, 'Topics to be included/deleted in the course to make it more effective are:'),
        (3, "Mention one or two of the faculty's most effective practices:"),
        (4, 'What additional constructive feedback can you offer to the faculty which might help the effectiveness of teaching?'),
    )
    comment_type = models.PositiveSmallIntegerField(choices=COMMENT_TYPE_CHOICES)
    comment = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=timezone.now)
    registration_number = models.CharField(max_length=16)
    course_name = models.CharField(max_length=75)
    course_id = models.CharField(max_length=16)
    section = models.CharField(max_length=2)
    faculty_name = models.CharField(max_length=50)
    faculty_id = models.IntegerField(null=True, blank=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        db_table = 'feedback_comments'

class Rating(models.Model):
    cfid = models.IntegerField(null=True, blank=True)
    faculty_rating = models.FloatField()
    course_rating = models.FloatField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ratings'
    
class Question(models.Model):
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
    type_of_course = models.CharField(max_length=1,choices=TYPE_OF_COURSE_CHOICES)
    question_for = models.CharField(max_length=1,choices=QUESTION_FOR_CHOICES)
    order = models.PositiveSmallIntegerField(null=False, blank=False)
    text = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        db_table = 'questions'

class UpdateSeen(models.Model):
    cid = models.IntegerField()
    faculty_id = models.IntegerField(null=True, blank=True)
    fseen = models.BooleanField(default=False)
    cseen = models.BooleanField(default=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        db_table = 'update_seen'

class FilledFeedback(models.Model):
    registration_number = models.CharField(max_length=16)
    timestamp = models.DateTimeField(default=timezone.now)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        db_table = 'filled_feedback'
