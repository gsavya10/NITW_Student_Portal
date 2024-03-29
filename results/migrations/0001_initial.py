# Generated by Django 2.1.2 on 2019-01-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedResults',
            fields=[
                ('roll', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'blocked_results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.IntegerField()),
                ('session_id', models.IntegerField()),
                ('specialization', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=128)),
                ('semester', models.IntegerField()),
                ('section', models.CharField(blank=True, max_length=10, null=True)),
                ('timestamp', models.DateTimeField()),
                ('publish_status', models.IntegerField()),
            ],
            options={
                'db_table': 'info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.IntegerField()),
                ('msno', models.IntegerField(blank=True, db_column='Msno', null=True)),
                ('batchcode', models.IntegerField(blank=True, db_column='BatchCode', null=True)),
                ('secname', models.CharField(blank=True, db_column='SecName', max_length=1, null=True)),
                ('degcode', models.IntegerField(blank=True, db_column='DegCode', null=True)),
                ('yrsemcode', models.IntegerField(blank=True, db_column='YrSemCode', null=True)),
                ('slno', models.IntegerField(blank=True, db_column='SlNo', null=True)),
                ('regno', models.IntegerField(blank=True, db_column='RegNo', null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=33, null=True)),
                ('grade1', models.CharField(blank=True, db_column='Grade1', max_length=2, null=True)),
                ('grade2', models.CharField(blank=True, db_column='Grade2', max_length=2, null=True)),
                ('grade3', models.CharField(blank=True, db_column='Grade3', max_length=2, null=True)),
                ('grade4', models.CharField(blank=True, db_column='Grade4', max_length=2, null=True)),
                ('grade5', models.CharField(blank=True, db_column='Grade5', max_length=2, null=True)),
                ('grade6', models.CharField(blank=True, db_column='Grade6', max_length=2, null=True)),
                ('grade7', models.CharField(blank=True, db_column='Grade7', max_length=2, null=True)),
                ('grade8', models.CharField(blank=True, db_column='Grade8', max_length=2, null=True)),
                ('grade9', models.CharField(blank=True, db_column='Grade9', max_length=2, null=True)),
                ('grade10', models.CharField(blank=True, db_column='Grade10', max_length=10, null=True)),
                ('grade11', models.CharField(blank=True, db_column='Grade11', max_length=10, null=True)),
                ('grade12', models.CharField(blank=True, db_column='Grade12', max_length=10, null=True)),
                ('grade13', models.CharField(blank=True, db_column='Grade13', max_length=10, null=True)),
                ('grade14', models.CharField(blank=True, db_column='Grade14', max_length=10, null=True)),
                ('sgpa', models.DecimalField(blank=True, db_column='Sgpa', decimal_places=2, max_digits=32, null=True)),
                ('cgpa', models.FloatField(blank=True, db_column='Cgpa', null=True)),
                ('totcr1', models.IntegerField(blank=True, db_column='TotCr1', null=True)),
                ('totcr2', models.IntegerField(blank=True, db_column='TotCr2', null=True)),
                ('nof1', models.IntegerField(blank=True, db_column='Nof1', null=True)),
                ('nof2', models.IntegerField(blank=True, db_column='Nof2', null=True)),
            ],
            options={
                'db_table': 'results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.IntegerField(unique=True)),
                ('code1', models.CharField(blank=True, max_length=7, null=True)),
                ('name1', models.CharField(blank=True, max_length=128, null=True)),
                ('aname1', models.CharField(blank=True, max_length=25, null=True)),
                ('credit1', models.CharField(blank=True, max_length=13, null=True)),
                ('code2', models.CharField(blank=True, max_length=10, null=True)),
                ('name2', models.CharField(blank=True, max_length=128, null=True)),
                ('aname2', models.CharField(blank=True, max_length=23, null=True)),
                ('credit2', models.CharField(blank=True, max_length=3, null=True)),
                ('code3', models.CharField(blank=True, max_length=24, null=True)),
                ('name3', models.CharField(blank=True, max_length=128, null=True)),
                ('aname3', models.CharField(blank=True, max_length=25, null=True)),
                ('credit3', models.CharField(blank=True, max_length=25, null=True)),
                ('code4', models.CharField(blank=True, max_length=21, null=True)),
                ('name4', models.CharField(blank=True, max_length=128, null=True)),
                ('aname4', models.CharField(blank=True, max_length=24, null=True)),
                ('credit4', models.CharField(blank=True, max_length=19, null=True)),
                ('code5', models.CharField(blank=True, max_length=13, null=True)),
                ('name5', models.CharField(blank=True, max_length=128, null=True)),
                ('aname5', models.CharField(blank=True, max_length=25, null=True)),
                ('credit5', models.CharField(blank=True, max_length=13, null=True)),
                ('code6', models.CharField(blank=True, max_length=7, null=True)),
                ('name6', models.CharField(blank=True, max_length=128, null=True)),
                ('aname6', models.CharField(blank=True, max_length=25, null=True)),
                ('credit6', models.CharField(blank=True, max_length=2, null=True)),
                ('code7', models.CharField(blank=True, max_length=20, null=True)),
                ('name7', models.CharField(blank=True, max_length=128, null=True)),
                ('aname7', models.CharField(blank=True, max_length=24, null=True)),
                ('credit7', models.CharField(blank=True, max_length=25, null=True)),
                ('code8', models.CharField(blank=True, max_length=16, null=True)),
                ('name8', models.CharField(blank=True, max_length=128, null=True)),
                ('aname8', models.CharField(blank=True, max_length=22, null=True)),
                ('credit8', models.CharField(blank=True, max_length=1, null=True)),
                ('code9', models.CharField(blank=True, max_length=7, null=True)),
                ('name9', models.CharField(blank=True, max_length=128, null=True)),
                ('aname9', models.CharField(blank=True, max_length=16, null=True)),
                ('credit9', models.CharField(blank=True, max_length=1, null=True)),
                ('code10', models.CharField(blank=True, max_length=6, null=True)),
                ('name10', models.CharField(blank=True, max_length=128, null=True)),
                ('aname10', models.CharField(blank=True, max_length=10, null=True)),
                ('credit10', models.CharField(blank=True, max_length=1, null=True)),
                ('code11', models.CharField(blank=True, max_length=10, null=True)),
                ('name11', models.CharField(blank=True, max_length=128, null=True)),
                ('aname11', models.CharField(blank=True, max_length=10, null=True)),
                ('credit11', models.CharField(blank=True, max_length=10, null=True)),
                ('code12', models.CharField(blank=True, max_length=10, null=True)),
                ('name12', models.CharField(blank=True, max_length=128, null=True)),
                ('aname12', models.CharField(blank=True, max_length=10, null=True)),
                ('credit12', models.CharField(blank=True, max_length=10, null=True)),
                ('code13', models.CharField(blank=True, max_length=10, null=True)),
                ('name13', models.CharField(blank=True, max_length=128, null=True)),
                ('aname13', models.CharField(blank=True, max_length=10, null=True)),
                ('credit13', models.CharField(blank=True, max_length=10, null=True)),
                ('code14', models.CharField(blank=True, max_length=10, null=True)),
                ('name14', models.CharField(blank=True, max_length=128, null=True)),
                ('aname14', models.CharField(blank=True, max_length=10, null=True)),
                ('credit14', models.CharField(blank=True, max_length=10, null=True)),
                ('semester', models.CharField(blank=True, max_length=19, null=True)),
                ('department', models.CharField(blank=True, max_length=41, null=True)),
                ('specialization', models.CharField(blank=True, max_length=38, null=True)),
                ('class_field', models.CharField(blank=True, db_column='class', max_length=33, null=True)),
                ('section', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'subjects',
                'managed': False,
            },
        ),
    ]
