# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser


class BioTech(models.Model):
	sl_no = models.IntegerField(db_column='Sl. No', blank=True,
	                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	regno = models.IntegerField(db_column='regNo', blank=True, null=True)  # Field name made lowercase.
	rollno = models.IntegerField(db_column='rollNo', blank=True, null=True)  # Field name made lowercase.
	name = models.CharField(db_column='Name', max_length=31, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Bio-tech'


class Ce(models.Model):
	sl_no = models.CharField(db_column='Sl. No', max_length=27, blank=True,
	                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	regno = models.CharField(db_column='regNo', max_length=6, blank=True, null=True)  # Field name made lowercase.
	rollno = models.CharField(db_column='rollNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
	name = models.CharField(db_column='Name', max_length=41, blank=True, null=True)  # Field name made lowercase.
	section = models.CharField(db_column='Section', max_length=7, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'CE'


class Cse(models.Model):
	sl_no = models.IntegerField(db_column='Sl. No', blank=True,
	                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	regno = models.IntegerField(db_column='regNo', blank=True, null=True)  # Field name made lowercase.
	rollno = models.IntegerField(db_column='rollNo', blank=True, null=True)  # Field name made lowercase.
	name = models.CharField(db_column='Name', max_length=34, blank=True, null=True)  # Field name made lowercase.
	section = models.CharField(db_column='Section', max_length=1, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'CSE'


class Chemical(models.Model):
	sl_no = models.IntegerField(db_column='Sl. No', blank=True,
	                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	regno = models.IntegerField(db_column='regNo', blank=True, null=True)  # Field name made lowercase.
	rollno = models.IntegerField(db_column='rollNo', blank=True, null=True)  # Field name made lowercase.
	name = models.CharField(db_column='Name', max_length=35, blank=True, null=True)  # Field name made lowercase.
	section = models.CharField(db_column='Section', max_length=1, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Chemical'


class Ece(models.Model):
	sl_no = models.IntegerField(db_column='Sl. No', blank=True,
	                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	regno = models.IntegerField(db_column='regNo', blank=True, null=True)  # Field name made lowercase.
	rollno = models.IntegerField(db_column='rollNo', blank=True, null=True)  # Field name made lowercase.
	name = models.CharField(db_column='Name', max_length=31, blank=True, null=True)  # Field name made lowercase.
	section = models.CharField(db_column='Section', max_length=1, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'ECE'


class Ee(models.Model):
	sl_no = models.IntegerField(db_column='Sl. No', blank=True,
	                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	regno = models.IntegerField(db_column='regNo', blank=True, null=True)  # Field name made lowercase.
	rollno = models.IntegerField(db_column='rollNo', blank=True, null=True)  # Field name made lowercase.
	name = models.CharField(db_column='Name', max_length=39, blank=True, null=True)  # Field name made lowercase.
	section = models.CharField(db_column='Section', max_length=1, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'EE'


class Me(models.Model):
	sl_no = models.IntegerField(db_column='Sl. No', blank=True,
	                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	regno = models.IntegerField(db_column='regNo', blank=True, null=True)  # Field name made lowercase.
	rollno = models.IntegerField(db_column='rollNo', blank=True, null=True)  # Field name made lowercase.
	name = models.CharField(db_column='Name', max_length=48, blank=True, null=True)  # Field name made lowercase.
	section = models.CharField(db_column='Section', max_length=1, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'ME'


class Mme(models.Model):
	sl_no = models.IntegerField(db_column='Sl. No', blank=True,
	                            null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	regno = models.IntegerField(db_column='regNo', blank=True, null=True)  # Field name made lowercase.
	rollno = models.IntegerField(db_column='rollNo', blank=True, null=True)  # Field name made lowercase.
	name = models.CharField(db_column='Name', max_length=36, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'MME'


class CiSessions(models.Model):
	session_id = models.CharField(primary_key=True, max_length=40)
	userid = models.IntegerField()
	ip_address = models.CharField(max_length=45)
	user_agent = models.CharField(max_length=120)
	last_activity = models.PositiveIntegerField()
	user_data = models.TextField()

	class Meta:
		managed = False
		db_table = 'ci_sessions'


class CouncilCredentials(models.Model):
	regno = models.CharField(max_length=10)
	username = models.CharField(max_length=10)
	password = models.CharField(max_length=10)

	class Meta:
		managed = False
		db_table = 'council_credentials'


class FeeRem(models.Model):
	roll = models.CharField(max_length=10)
	bank = models.CharField(max_length=100)
	acc = models.CharField(max_length=20)
	ifsc = models.CharField(max_length=20)

	class Meta:
		managed = False
		db_table = 'fee_rem'


class FirstYears(models.Model):
	id = models.IntegerField(blank=True, primary_key=True)
	roll_number = models.IntegerField(db_column='Roll_Number', blank=True, null=True)  # Field name made lowercase.
	name = models.CharField(db_column='Name', max_length=42, blank=True, null=True)  # Field name made lowercase.
	gender = models.CharField(db_column='Gender', max_length=6, blank=True, null=True)  # Field name made lowercase.
	branch = models.CharField(db_column='Branch', max_length=39, blank=True, null=True)  # Field name made lowercase.
	section = models.CharField(db_column='Section', max_length=1, blank=True, null=True)  # Field name made lowercase.
	mobile_number = models.BigIntegerField(db_column='Mobile_number', blank=True,
	                                       null=True)  # Field name made lowercase.
	email_id = models.CharField(db_column='Email_id', max_length=35, blank=True,
	                            null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'first_years'


# class Groups(models.Model):
#     name = models.CharField(max_length=20)
#     description = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'groups'


class LanRadio(models.Model):
	song_desc = models.TextField()

	class Meta:
		managed = False
		db_table = 'lan_radio'


class LanRadioIp(models.Model):
	id = models.IntegerField(primary_key=True)
	ip_address = models.CharField(max_length=48)
	port = models.CharField(max_length=4)
	stream = models.CharField(max_length=32)

	class Meta:
		managed = False
		db_table = 'lan_radio_ip'


class LoginAttempts(models.Model):
	ip_address = models.CharField(max_length=15)
	login = models.CharField(max_length=100)
	time = models.PositiveIntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'login_attempts'


class Macs(models.Model):
	userid = models.IntegerField(primary_key=True)
	last_updated = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'macs'


class Mail(models.Model):
	sno = models.AutoField(primary_key=True)
	registration_number = models.CharField(max_length=10, blank=True, null=True)
	email_id = models.CharField(max_length=100, blank=True, null=True)
	password = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'mail'


class Mail2017(models.Model):
	roll = models.CharField(max_length=10)
	reg = models.CharField(max_length=10)
	name = models.CharField(max_length=100)
	email_id = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	terms_accepted = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'mail_2017'
		unique_together = (('roll', 'reg'),)


class MailAll(models.Model):
	sno = models.AutoField(primary_key=True)
	registration_number = models.CharField(max_length=10, blank=True, null=True)
	email_id = models.CharField(max_length=100, blank=True, null=True)
	password = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'mail_all'


class MailOld(models.Model):
	sr_no = models.CharField(max_length=11, blank=True, null=True)
	email_id = models.CharField(max_length=36, blank=True, null=True)
	first_name = models.CharField(max_length=35, blank=True, null=True)
	last_name = models.CharField(max_length=29, blank=True, null=True)
	registration_number = models.CharField(max_length=11, blank=True, null=True)
	roll_number = models.CharField(max_length=13, blank=True, null=True)
	secondary_email = models.CharField(max_length=43, blank=True, null=True)
	work_phone = models.CharField(max_length=12, blank=True, null=True)
	department = models.CharField(max_length=10, blank=True, null=True)
	employee_type = models.CharField(max_length=13, blank=True, null=True)
	password = models.CharField(max_length=16, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'mail_old'


class MessChange(models.Model):
	regno = models.CharField(max_length=8, blank=True, null=True)
	from_field = models.CharField(db_column='from', max_length=16, blank=True,
	                              null=True)  # Field renamed because it was a Python reserved word.
	to = models.CharField(max_length=9, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'mess_change'


class MtechFirstYears(models.Model):
	reg_no = models.CharField(db_column='Reg No', max_length=7, blank=True,
	                          null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	roll_number = models.CharField(db_column='Roll_number', max_length=8, blank=True,
	                               null=True)  # Field name made lowercase.
	name = models.CharField(db_column='Name', max_length=33, blank=True, null=True)  # Field name made lowercase.
	father_name = models.CharField(db_column='Father Name', max_length=27, blank=True,
	                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	mother_name = models.CharField(db_column='Mother Name', max_length=28, blank=True,
	                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	course = models.CharField(db_column='Course', max_length=7, blank=True, null=True)  # Field name made lowercase.
	branch = models.CharField(db_column='Branch', max_length=39, blank=True, null=True)  # Field name made lowercase.
	gate_score = models.IntegerField(db_column='Gate Score', blank=True,
	                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	aadhar_number = models.BigIntegerField(db_column='Aadhar Number', blank=True,
	                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	religion = models.CharField(db_column='Religion', max_length=9, blank=True, null=True)  # Field name made lowercase.
	category = models.CharField(db_column='Category', max_length=7, blank=True, null=True)  # Field name made lowercase.
	gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
	address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
	mobile_number = models.BigIntegerField(db_column='Mobile_number', blank=True,
	                                       null=True)  # Field name made lowercase.
	email_id = models.CharField(db_column='Email_id', max_length=35, blank=True,
	                            null=True)  # Field name made lowercase.
	date_of_adm_field = models.CharField(db_column='Date of Adm.', max_length=9, blank=True,
	                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
	blood_group = models.CharField(db_column='Blood Group', max_length=5, blank=True,
	                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	dob = models.CharField(db_column='DOB', max_length=10, blank=True, null=True)  # Field name made lowercase.
	father_mobile_no = models.BigIntegerField(db_column='Father Mobile No', blank=True,
	                                          null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

	class Meta:
		managed = False
		db_table = 'mtech_first_years'


class MtechNew(models.Model):
	rollno = models.CharField(db_column='rollNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
	regno = models.CharField(db_column='regNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
	c = models.CharField(db_column='C', max_length=37, blank=True, null=True)  # Field name made lowercase.
	d = models.CharField(db_column='D', max_length=39, blank=True, null=True)  # Field name made lowercase.
	e = models.CharField(db_column='E', max_length=22, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'mtech_new'


class Office365(models.Model):
	regno = models.CharField(max_length=10)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)

	class Meta:
		managed = False
		db_table = 'office365'


class StudentData(models.Model):
	userid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64)
	roll_number = models.CharField(unique=True, max_length=10, blank=True, null=True)
	registration_number = models.CharField(unique=True, max_length=10, blank=True, null=True)
	current_section = models.CharField(max_length=4)
	current_year = models.CharField(max_length=4)
	joining_year = models.CharField(max_length=4)
	course = models.CharField(max_length=10)
	branch = models.CharField(max_length=10)
	gender = models.CharField(max_length=1)
	birthday = models.DateField()
	country = models.CharField(max_length=32)
	mobile = models.CharField(max_length=16)
	emergency_contact = models.CharField(max_length=16)
	sbh_account = models.CharField(max_length=32, blank=True, null=True)
	passport = models.CharField(max_length=20, blank=True, null=True)
	hostel_room = models.CharField(max_length=10)
	hostel = models.CharField(max_length=10)
	mess = models.CharField(max_length=10)
	created_location = models.CharField(max_length=32)
	created_time = models.DateTimeField()
	guardian1 = models.CharField(max_length=64, blank=True, null=True)
	relationship1 = models.CharField(max_length=64, blank=True, null=True)
	email1 = models.CharField(max_length=64, blank=True, null=True)
	mobile1 = models.CharField(max_length=16, blank=True, null=True)
	guardian2 = models.CharField(max_length=64, blank=True, null=True)
	relationship2 = models.CharField(max_length=64, blank=True, null=True)
	email2 = models.CharField(max_length=64, blank=True, null=True)
	mobile2 = models.CharField(max_length=16, blank=True, null=True)
	homenumber = models.CharField(max_length=16, blank=True, null=True)
	address = models.CharField(max_length=500, blank=True, null=True)
	bloodgroup = models.CharField(max_length=5, blank=True, null=True)
	adhaar = models.CharField(max_length=20, blank=True, null=True)
	linkedin = models.CharField(max_length=100, blank=True, null=True)
	mac = models.CharField(max_length=30, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'student_data'
		unique_together = (('roll_number', 'registration_number'),)


class Temp(models.Model):
	roll = models.CharField(max_length=7, blank=True, null=True)
	reg = models.CharField(max_length=10)

	class Meta:
		managed = False
		db_table = 'temp'


class Tzcodes(models.Model):
	rollno = models.IntegerField(primary_key=True)
	code = models.CharField(max_length=15)
	isused = models.IntegerField(db_column='isUsed')  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'tzCodes'


class Users(AbstractUser):
	ip_address = models.CharField(max_length=15)
	username = models.CharField(unique=True, max_length=100)
	password = models.CharField(max_length=255)
	profile_edited = models.IntegerField()
	salt = models.CharField(max_length=40, blank=True, null=True)
	email = models.CharField(unique=True, max_length=100)
	activation_code = models.CharField(max_length=40, blank=True, null=True)
	forgotten_password_code = models.CharField(max_length=40, blank=True, null=True)
	forgotten_password_time = models.PositiveIntegerField(blank=True, null=True)
	remember_code = models.CharField(max_length=40, blank=True, null=True)
	created_on = models.PositiveIntegerField()
	last_login = models.DateTimeField(blank=True, null=True)
	active = models.PositiveIntegerField(blank=True, null=True)
	first_name = models.CharField(max_length=50, blank=True, null=True)
	middle_name = models.CharField(max_length=256)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	company = models.CharField(max_length=100, blank=True, null=True)
	phone = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		db_table = 'users'

	def get_student_data(self):
		return StudentData.objects.filter(userid=self.id).first()

# class UsersGroups(models.Model):
#     user = models.ForeignKey(Users, models.DO_NOTHING)
#     group = models.ForeignKey(Groups, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'users_groups'
#         unique_together = (('user', 'group'),)
