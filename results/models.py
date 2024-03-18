# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from registration.models import RegistrationDbManager


class ResultsManager(models.Manager):
    using = 'wsdc_results'

    def get_queryset(self):
        return super(ResultsManager, self).get_queryset().using(self.using)


class BlockedResults(models.Model):
    roll = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'blocked_results'

    objects = ResultsManager()


class Info(models.Model):
    reference_id = models.IntegerField(primary_key=True)
    session_id = models.IntegerField()
    specialization = models.CharField(max_length=20)
    branch = models.CharField(max_length=128)
    semester = models.IntegerField()
    section = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.DateTimeField()
    publish_status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'info'

    objects = ResultsManager()


class Results(models.Model):
    reference_id = models.AutoField(primary_key=True)
    msno = models.IntegerField(db_column='Msno', blank=True, null=True)  # Field name made lowercase.
    batchcode = models.IntegerField(db_column='BatchCode', blank=True, null=True)  # Field name made lowercase.
    secname = models.CharField(db_column='SecName', max_length=1, blank=True, null=True)  # Field name made lowercase.
    degcode = models.IntegerField(db_column='DegCode', blank=True, null=True)  # Field name made lowercase.
    yrsemcode = models.IntegerField(db_column='YrSemCode', blank=True, null=True)  # Field name made lowercase.
    slno = models.IntegerField(db_column='SlNo', blank=True, null=True)  # Field name made lowercase.
    regno = models.CharField(max_length=20, db_column='RegNo', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=33, blank=True, null=True)  # Field name made lowercase.
    grade1 = models.CharField(db_column='Grade1', max_length=2, blank=True, null=True)  # Field name made lowercase.
    grade2 = models.CharField(db_column='Grade2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    grade3 = models.CharField(db_column='Grade3', max_length=2, blank=True, null=True)  # Field name made lowercase.
    grade4 = models.CharField(db_column='Grade4', max_length=2, blank=True, null=True)  # Field name made lowercase.
    grade5 = models.CharField(db_column='Grade5', max_length=2, blank=True, null=True)  # Field name made lowercase.
    grade6 = models.CharField(db_column='Grade6', max_length=2, blank=True, null=True)  # Field name made lowercase.
    grade7 = models.CharField(db_column='Grade7', max_length=2, blank=True, null=True)  # Field name made lowercase.
    grade8 = models.CharField(db_column='Grade8', max_length=2, blank=True, null=True)  # Field name made lowercase.
    grade9 = models.CharField(db_column='Grade9', max_length=2, blank=True, null=True)  # Field name made lowercase.
    grade10 = models.CharField(db_column='Grade10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    grade11 = models.CharField(db_column='Grade11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    grade12 = models.CharField(db_column='Grade12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    grade13 = models.CharField(db_column='Grade13', max_length=10, blank=True, null=True)  # Field name made lowercase.
    grade14 = models.CharField(db_column='Grade14', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sgpa = models.DecimalField(db_column='Sgpa', max_digits=32, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cgpa = models.FloatField(db_column='Cgpa', blank=True, null=True)  # Field name made lowercase.
    totcr1 = models.IntegerField(db_column='TotCr1', blank=True, null=True)  # Field name made lowercase.
    totcr2 = models.IntegerField(db_column='TotCr2', blank=True, null=True)  # Field name made lowercase.
    nof1 = models.IntegerField(db_column='Nof1', blank=True, null=True)  # Field name made lowercase.
    nof2 = models.IntegerField(db_column='Nof2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'results'

    objects = ResultsManager()


class Subjects(models.Model):
    reference_id = models.AutoField(unique=True, primary_key=True)
    code1 = models.CharField(max_length=7, blank=True, null=True)
    name1 = models.CharField(max_length=128, blank=True, null=True)
    aname1 = models.CharField(max_length=25, blank=True, null=True)
    credit1 = models.CharField(max_length=13, blank=True, null=True)
    code2 = models.CharField(max_length=10, blank=True, null=True)
    name2 = models.CharField(max_length=128, blank=True, null=True)
    aname2 = models.CharField(max_length=23, blank=True, null=True)
    credit2 = models.CharField(max_length=3, blank=True, null=True)
    code3 = models.CharField(max_length=24, blank=True, null=True)
    name3 = models.CharField(max_length=128, blank=True, null=True)
    aname3 = models.CharField(max_length=25, blank=True, null=True)
    credit3 = models.CharField(max_length=25, blank=True, null=True)
    code4 = models.CharField(max_length=21, blank=True, null=True)
    name4 = models.CharField(max_length=128, blank=True, null=True)
    aname4 = models.CharField(max_length=24, blank=True, null=True)
    credit4 = models.CharField(max_length=19, blank=True, null=True)
    code5 = models.CharField(max_length=13, blank=True, null=True)
    name5 = models.CharField(max_length=128, blank=True, null=True)
    aname5 = models.CharField(max_length=25, blank=True, null=True)
    credit5 = models.CharField(max_length=13, blank=True, null=True)
    code6 = models.CharField(max_length=7, blank=True, null=True)
    name6 = models.CharField(max_length=128, blank=True, null=True)
    aname6 = models.CharField(max_length=25, blank=True, null=True)
    credit6 = models.CharField(max_length=2, blank=True, null=True)
    code7 = models.CharField(max_length=20, blank=True, null=True)
    name7 = models.CharField(max_length=128, blank=True, null=True)
    aname7 = models.CharField(max_length=24, blank=True, null=True)
    credit7 = models.CharField(max_length=25, blank=True, null=True)
    code8 = models.CharField(max_length=16, blank=True, null=True)
    name8 = models.CharField(max_length=128, blank=True, null=True)
    aname8 = models.CharField(max_length=22, blank=True, null=True)
    credit8 = models.CharField(max_length=1, blank=True, null=True)
    code9 = models.CharField(max_length=7, blank=True, null=True)
    name9 = models.CharField(max_length=128, blank=True, null=True)
    aname9 = models.CharField(max_length=16, blank=True, null=True)
    credit9 = models.CharField(max_length=1, blank=True, null=True)
    code10 = models.CharField(max_length=6, blank=True, null=True)
    name10 = models.CharField(max_length=128, blank=True, null=True)
    aname10 = models.CharField(max_length=10, blank=True, null=True)
    credit10 = models.CharField(max_length=1, blank=True, null=True)
    code11 = models.CharField(max_length=10, blank=True, null=True)
    name11 = models.CharField(max_length=128, blank=True, null=True)
    aname11 = models.CharField(max_length=10, blank=True, null=True)
    credit11 = models.CharField(max_length=10, blank=True, null=True)
    code12 = models.CharField(max_length=10, blank=True, null=True)
    name12 = models.CharField(max_length=128, blank=True, null=True)
    aname12 = models.CharField(max_length=10, blank=True, null=True)
    credit12 = models.CharField(max_length=10, blank=True, null=True)
    code13 = models.CharField(max_length=10, blank=True, null=True)
    name13 = models.CharField(max_length=128, blank=True, null=True)
    aname13 = models.CharField(max_length=10, blank=True, null=True)
    credit13 = models.CharField(max_length=10, blank=True, null=True)
    code14 = models.CharField(max_length=10, blank=True, null=True)
    name14 = models.CharField(max_length=128, blank=True, null=True)
    aname14 = models.CharField(max_length=10, blank=True, null=True)
    credit14 = models.CharField(max_length=10, blank=True, null=True)
    semester = models.CharField(max_length=19, blank=True, null=True)
    department = models.CharField(max_length=41, blank=True, null=True)
    specialization = models.CharField(max_length=38, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=33, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    section = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'subjects'

    objects = ResultsManager()


class Session(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    last_modified_on = models.DateTimeField()
    results_publish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'session'

    objects = RegistrationDbManager()
