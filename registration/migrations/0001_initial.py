# Generated by Django 2.1.2 on 2018-10-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedstudentsregDayscholars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(db_column='RegNo', max_length=11)),
            ],
            options={
                'db_table': 'AllowedstudentsReg_dayscholars',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('structure_id', models.IntegerField()),
                ('course_id', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=2)),
                ('lab_batch', models.IntegerField()),
                ('date', models.DateField()),
                ('no_hours', models.DecimalField(decimal_places=2, max_digits=11)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
            options={
                'db_table': 'attendance_dates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('count', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('rollno', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'attendance_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BlockStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=25)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'block_student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_id', models.IntegerField(blank=True, null=True)),
                ('reg_structure_id', models.IntegerField(blank=True, null=True)),
                ('reg_session_id', models.IntegerField(blank=True, null=True)),
                ('reg_session_name', models.CharField(blank=True, max_length=128, null=True)),
                ('reg_department_id', models.IntegerField(blank=True, null=True)),
                ('reg_department_name', models.CharField(blank=True, max_length=100, null=True)),
                ('reg_specialization_id', models.IntegerField(blank=True, null=True)),
                ('reg_specialization_name', models.CharField(blank=True, max_length=256, null=True)),
                ('reg_semester', models.IntegerField(blank=True, null=True)),
                ('reg_section', models.CharField(blank=True, max_length=2, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=10, null=True)),
                ('structure_id', models.IntegerField(blank=True, null=True)),
                ('section', models.CharField(blank=True, max_length=2, null=True)),
                ('course_id', models.CharField(blank=True, max_length=9, null=True)),
                ('course_name', models.CharField(blank=True, max_length=67, null=True)),
                ('credit', models.IntegerField(blank=True, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('course_type_name', models.CharField(blank=True, max_length=100, null=True)),
                ('batch', models.IntegerField(blank=True, null=True)),
                ('mode', models.IntegerField(blank=True, null=True)),
                ('backlog', models.IntegerField(blank=True, null=True)),
                ('registered_on', models.DateTimeField(blank=True, null=True)),
                ('last_modified_on', models.DateTimeField()),
                ('pre_registered', models.IntegerField(blank=True, null=True)),
                ('approved', models.IntegerField(blank=True, null=True)),
                ('academic_fee_status', models.IntegerField(blank=True, null=True)),
                ('hostel_fee_status', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'comp_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CourseAllottedMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'course_allotted_mode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CourseFacultyAllotted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular_course_id', models.IntegerField()),
                ('section', models.CharField(max_length=2)),
                ('batch_index', models.IntegerField()),
                ('faculty_id', models.IntegerField(blank=True, null=True)),
                ('last_modified_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'course_faculty_allotted',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=67)),
                ('credit', models.IntegerField()),
                ('type', models.IntegerField()),
                ('last_modified_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'courses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CoursesType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_modified_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'courses_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_modified_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DepartmentSpecialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.IntegerField()),
                ('specialization_id', models.IntegerField()),
            ],
            options={
                'db_table': 'department_specialization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailedDepartmentSpecialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.IntegerField(blank=True, null=True)),
                ('department_name', models.CharField(blank=True, max_length=100, null=True)),
                ('specialization_id', models.IntegerField(blank=True, null=True)),
                ('specialization_name', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'detailed_department_specialization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailedRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_id', models.IntegerField(blank=True, null=True)),
                ('reg_structure_id', models.IntegerField(blank=True, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=10, null=True)),
                ('reg_section', models.CharField(blank=True, max_length=2, null=True)),
                ('pre_registered', models.IntegerField(blank=True, null=True)),
                ('approved', models.IntegerField(blank=True, null=True)),
                ('academic_fee_status', models.IntegerField(blank=True, null=True)),
                ('hostel_fee_status', models.IntegerField(blank=True, null=True)),
                ('reg_session_id', models.IntegerField(blank=True, null=True)),
                ('reg_session_name', models.CharField(blank=True, max_length=128, null=True)),
                ('reg_department_id', models.IntegerField(blank=True, null=True)),
                ('reg_department_name', models.CharField(blank=True, max_length=100, null=True)),
                ('reg_specialization_id', models.IntegerField(blank=True, null=True)),
                ('reg_specialization_name', models.CharField(blank=True, max_length=256, null=True)),
                ('reg_semester', models.IntegerField(blank=True, null=True)),
                ('course_id', models.CharField(blank=True, max_length=9, null=True)),
                ('batch', models.IntegerField(blank=True, null=True)),
                ('mode', models.IntegerField(blank=True, null=True)),
                ('registered_on', models.DateTimeField(blank=True, null=True)),
                ('last_modified_on', models.DateTimeField()),
                ('backlog', models.IntegerField(blank=True, null=True)),
                ('course_name', models.CharField(blank=True, max_length=67, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('credit', models.IntegerField(blank=True, null=True)),
                ('course_type_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'detailed_registration',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailedStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('structure_id', models.IntegerField(blank=True, null=True)),
                ('faculty_id', models.IntegerField(blank=True, null=True)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('department_id', models.IntegerField(blank=True, null=True)),
                ('department_name', models.CharField(blank=True, max_length=100, null=True)),
                ('specialization_id', models.IntegerField(blank=True, null=True)),
                ('specialization_name', models.CharField(blank=True, max_length=256, null=True)),
                ('session_id', models.IntegerField(blank=True, null=True)),
                ('session_name', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'detailed_structure',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExamOnly',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('regno2', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'exam_only',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FeesPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=100, unique=True)),
                ('hostel_fees_status', models.IntegerField()),
                ('amount_to_be_paid', models.IntegerField()),
                ('student_paid', models.IntegerField()),
                ('faculty_advisor_approved', models.IntegerField()),
            ],
            options={
                'db_table': 'fees_payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Registered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=10)),
                ('reg_structure_id', models.IntegerField()),
                ('reg_section', models.CharField(max_length=2)),
                ('pre_registered', models.IntegerField()),
                ('approved', models.IntegerField()),
                ('academic_fee_status', models.IntegerField()),
                ('hostel_fee_status', models.IntegerField()),
            ],
            options={
                'db_table': 'registered',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegisteredCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_id', models.IntegerField()),
                ('structure_id', models.IntegerField()),
                ('section', models.CharField(max_length=2)),
                ('course_id', models.CharField(max_length=9)),
                ('batch', models.IntegerField()),
                ('mode', models.IntegerField()),
                ('backlog', models.IntegerField()),
                ('registered_on', models.DateTimeField()),
                ('last_modified_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'registered_courses',
                'managed': False,
            },
        ),
    ]
