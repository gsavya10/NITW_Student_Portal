# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# Create your models here.


class RegistrationDbManager(models.Manager):
    using = 'registration'

    def get_queryset(self):
        return super(RegistrationDbManager, self).get_queryset().using(self.using)


class AllowedstudentsregDayscholars(models.Model):
    regno = models.CharField(db_column='RegNo', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AllowedstudentsReg_dayscholars'

    objects =RegistrationDbManager()


class AttendanceDates(models.Model):
    structure_id = models.IntegerField()
    course_id = models.CharField(max_length=10)
    section = models.CharField(max_length=2)
    lab_batch = models.IntegerField()
    date = models.DateField()
    no_hours = models.DecimalField(max_digits=11, decimal_places=2)
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        managed = False
        db_table = 'attendance_dates'

    objects =RegistrationDbManager()



class AttendanceRecord(models.Model):
    count = models.AutoField(primary_key=True)
    id = models.IntegerField()
    rollno = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'attendance_record'

    objects =RegistrationDbManager()



class BlockStudent(models.Model):
    reg_no = models.CharField(max_length=25)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'block_student'

    objects =RegistrationDbManager()



class CompData(models.Model):
    registered_id = models.IntegerField(blank=True, null=True)
    reg_structure_id = models.IntegerField(blank=True, null=True)
    reg_session_id = models.IntegerField(blank=True, null=True)
    reg_session_name = models.CharField(max_length=128, blank=True, null=True)
    reg_department_id = models.IntegerField(blank=True, null=True)
    reg_department_name = models.CharField(max_length=100, blank=True, null=True)
    reg_specialization_id = models.IntegerField(blank=True, null=True)
    reg_specialization_name = models.CharField(max_length=256, blank=True, null=True)
    reg_semester = models.IntegerField(blank=True, null=True)
    reg_section = models.CharField(max_length=2, blank=True, null=True)
    registration_number = models.CharField(max_length=10, blank=True, null=True)
    structure_id = models.IntegerField(blank=True, null=True)
    section = models.CharField(max_length=2, blank=True, null=True)
    course_id = models.CharField(max_length=9, blank=True, null=True)
    course_name = models.CharField(max_length=67, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    course_type_name = models.CharField(max_length=100, blank=True, null=True)
    batch = models.IntegerField(blank=True, null=True)
    mode = models.IntegerField(blank=True, null=True)
    backlog = models.IntegerField(blank=True, null=True)
    registered_on = models.DateTimeField(blank=True, null=True)
    last_modified_on = models.DateTimeField()
    pre_registered = models.IntegerField(blank=True, null=True)
    approved = models.IntegerField(blank=True, null=True)
    academic_fee_status = models.IntegerField(blank=True, null=True)
    hostel_fee_status = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comp_data'

    objects =RegistrationDbManager()


class CourseAllottedMode(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'course_allotted_mode'

    objects =RegistrationDbManager()


class CourseFacultyAllotted(models.Model):
    regular_course_id = models.IntegerField()
    section = models.CharField(max_length=2)
    batch_index = models.IntegerField()
    faculty_id = models.IntegerField(blank=True, null=True)
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'course_faculty_allotted'
        unique_together = (('regular_course_id', 'section', 'batch_index'),)

    objects =RegistrationDbManager()



class Courses(models.Model):
    id = models.CharField(primary_key=True, max_length=9)
    name = models.CharField(max_length=67)
    credit = models.IntegerField()
    type = models.IntegerField()
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'courses'

    objects =RegistrationDbManager()



class CoursesType(models.Model):
    name = models.CharField(max_length=100)
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'courses_type'

    objects =RegistrationDbManager()



class Department(models.Model):
    name = models.CharField(max_length=100)
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'department'

    objects =RegistrationDbManager()


class DepartmentSpecialization(models.Model):
    department_id = models.IntegerField()
    specialization_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'department_specialization'
        unique_together = (('department_id', 'specialization_id'),)

    objects =RegistrationDbManager()



class ExamOnly(models.Model):
    sno = models.AutoField(primary_key=True)
    regno2 = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'exam_only'

    objects =RegistrationDbManager()



class FeesPayment(models.Model):
    reg_no = models.CharField(unique=True, max_length=100)
    hostel_fees_status = models.IntegerField()
    amount_to_be_paid = models.IntegerField()
    student_paid = models.IntegerField()
    faculty_advisor_approved = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fees_payment'

    objects =RegistrationDbManager()



class Registered(models.Model):
    registration_number = models.CharField(max_length=10)
    reg_structure = models.ForeignKey('Structure', models.DO_NOTHING)
    reg_section = models.ForeignKey('Section', models.DO_NOTHING, db_column='reg_section')
    pre_registered = models.IntegerField()
    approved = models.IntegerField()
    academic_fee_status = models.IntegerField()
    hostel_fee_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registered'
        unique_together = (('registration_number', 'reg_structure'),)


    objects =RegistrationDbManager()

  

class RegisteredCourses(models.Model):
    registered = models.ForeignKey(Registered, models.DO_NOTHING)
    structure = models.ForeignKey('Structure', models.DO_NOTHING)
    section = models.ForeignKey('Section', models.DO_NOTHING, db_column='section')
    course = models.ForeignKey(Courses, models.DO_NOTHING)
    batch = models.IntegerField()
    mode = models.ForeignKey('RegisteredMode', models.DO_NOTHING, db_column='mode')
    backlog = models.IntegerField()
    registered_on = models.DateTimeField()
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registered_courses'
        unique_together = (('registered', 'structure', 'course', 'backlog'),)

    objects =RegistrationDbManager()



class RegisteredMode(models.Model):
    name = models.CharField(max_length=20)
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registered_mode'

    objects =RegistrationDbManager()



class RegularCourses(models.Model):
    structure_id = models.IntegerField()
    course_id = models.CharField(max_length=9)
    course_mode = models.IntegerField()
    last_modified_on = models.DateTimeField()

    class Meta: 
        managed = False
        db_table = 'regular_courses'
        unique_together = (('structure_id', 'course_id'),)

    objects =RegistrationDbManager()



class Section(models.Model):
    id = models.CharField(primary_key=True, max_length=2)

    class Meta:
        managed = False
        db_table = 'section'

    objects =RegistrationDbManager()



class Session(models.Model):
    name = models.CharField(max_length=128)
    last_modified_on = models.DateTimeField()
    results_publish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'session'

    objects =RegistrationDbManager()



class Specialization(models.Model):
    abbr = models.CharField(max_length=16)
    name = models.CharField(max_length=256)
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'specialization'

    objects =RegistrationDbManager()



class Structure(models.Model):
    faculty_id = models.IntegerField(blank=True, null=True)
    session_id = models.IntegerField()
    department_id = models.IntegerField()
    specialization_id = models.IntegerField()
    semester = models.IntegerField()
    last_modified_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'structure'
        unique_together = (('session_id', 'department_id', 'specialization_id', 'semester'),)

    objects =RegistrationDbManager()



class StructureSection(models.Model):
    structure_id = models.IntegerField()
    section = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'structure_section'
        unique_together = (('structure_id', 'section'),)

    objects =RegistrationDbManager()



class Temp(models.Model):
    col_1 = models.CharField(db_column='COL 1', max_length=37, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_2 = models.CharField(db_column='COL 2', max_length=7, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_3 = models.CharField(db_column='COL 3', max_length=7, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_4 = models.CharField(db_column='COL 4', max_length=39, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_5 = models.CharField(db_column='COL 5', max_length=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_6 = models.CharField(db_column='COL 6', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cid = models.CharField(max_length=6, blank=True, null=True)
    cname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'temp'

    objects =RegistrationDbManager()



class Timestamp(models.Model):
    regno = models.CharField(max_length=10)
    time = models.DateTimeField()
    ip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'timestamp'

    objects =RegistrationDbManager()



class TimestampSession9(models.Model):
    regno = models.CharField(max_length=10)
    time = models.DateTimeField()
    ip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'timestamp_session_9'

    objects =RegistrationDbManager()
