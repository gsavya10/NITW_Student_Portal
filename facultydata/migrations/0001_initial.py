# Generated by Django 2.1.2 on 2019-01-15 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('department_code', models.IntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'departments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Factemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=28, null=True)),
                ('department', models.CharField(blank=True, max_length=40, null=True)),
                ('designation', models.CharField(blank=True, max_length=20, null=True)),
                ('facid', models.CharField(blank=True, max_length=5, null=True)),
                ('specialization', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'factemp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FacultyCurrentData',
            fields=[
                ('facultyid', models.AutoField(primary_key=True, serialize=False)),
                ('drupal_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=20)),
                ('interest', models.TextField()),
                ('department', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=5000, null=True)),
                ('phone', models.CharField(blank=True, max_length=256, null=True)),
                ('office', models.CharField(max_length=20)),
                ('officeaddress', models.CharField(max_length=5000)),
                ('extlinks', models.CharField(max_length=5000)),
                ('profile', models.TextField(blank=True, null=True)),
                ('edit', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField()),
                ('approve_ipaddress', models.CharField(max_length=50)),
                ('approve_by', models.CharField(max_length=50)),
                ('courses', models.TextField(blank=True, null=True)),
                ('phds', models.TextField(blank=True, null=True)),
                ('workshops', models.TextField(blank=True, null=True)),
                ('projects', models.TextField(blank=True, null=True)),
                ('awards', models.TextField(blank=True, null=True)),
                ('responsibility', models.TextField(blank=True, null=True)),
                ('publications', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'faculty_current_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FacultyCurrentData33',
            fields=[
                ('facultyid', models.AutoField(primary_key=True, serialize=False)),
                ('drupal_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=20)),
                ('interest', models.TextField()),
                ('department', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=5000, null=True)),
                ('phone', models.CharField(blank=True, max_length=256, null=True)),
                ('office', models.CharField(max_length=20)),
                ('officeaddress', models.CharField(max_length=5000)),
                ('extlinks', models.CharField(max_length=5000)),
                ('profile', models.TextField(blank=True, null=True)),
                ('edit', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField()),
                ('approve_ipaddress', models.CharField(max_length=50)),
                ('approve_by', models.CharField(max_length=50)),
                ('courses', models.TextField(blank=True, null=True)),
                ('phds', models.TextField(blank=True, null=True)),
                ('workshops', models.TextField(blank=True, null=True)),
                ('projects', models.TextField(blank=True, null=True)),
                ('awards', models.TextField(blank=True, null=True)),
                ('responsibility', models.TextField(blank=True, null=True)),
                ('publications', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'faculty_current_data33',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FacultyDesignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_code', models.IntegerField()),
                ('designation_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'faculty_designation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FacultyPendingData',
            fields=[
                ('facultyid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('interest', models.TextField()),
                ('phone', models.CharField(max_length=256)),
                ('office', models.CharField(max_length=100)),
                ('officeaddress', models.CharField(max_length=5000)),
                ('extlinks', models.CharField(max_length=5000)),
                ('email', models.CharField(max_length=100)),
                ('profile', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('review', models.IntegerField(blank=True, null=True)),
                ('saved', models.IntegerField()),
                ('ipaddress', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('courses', models.TextField(blank=True, null=True)),
                ('phds', models.TextField(blank=True, null=True)),
                ('workshops', models.TextField(blank=True, null=True)),
                ('projects', models.TextField(blank=True, null=True)),
                ('awards', models.TextField(blank=True, null=True)),
                ('responsibility', models.TextField(blank=True, null=True)),
                ('publications', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'faculty_pending_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LoginAttempts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=16)),
                ('login', models.CharField(max_length=100)),
                ('time', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'login_attempts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=80)),
                ('salt', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.CharField(max_length=100)),
                ('activation_code', models.CharField(blank=True, max_length=40, null=True)),
                ('forgotten_password_code', models.CharField(blank=True, max_length=40, null=True)),
                ('forgotten_password_time', models.PositiveIntegerField(blank=True, null=True)),
                ('remember_code', models.CharField(blank=True, max_length=40, null=True)),
                ('created_on', models.PositiveIntegerField()),
                ('last_login', models.PositiveIntegerField(blank=True, null=True)),
                ('active', models.PositiveIntegerField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('department_code', models.IntegerField()),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'users_groups',
                'managed': False,
            },
        ),
    ]
