# Generated by Django 4.2.10 on 2024-03-21 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hris', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time_in', models.DateTimeField(blank=True, default=datetime.time(0, 0), null=True)),
                ('break_in', models.DateTimeField(blank=True, default=datetime.time(0, 0), null=True)),
                ('break_out', models.DateTimeField(blank=True, default=datetime.time(0, 0), null=True)),
                ('time_out', models.DateTimeField(blank=True, default=datetime.time(0, 0), null=True)),
                ('surplusHour_time_in', models.DateTimeField(blank=True, default=datetime.time(0, 0), null=True)),
                ('surplusHour_time_out', models.DateTimeField(blank=True, default=datetime.time(0, 0), null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfficialTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20)),
                ('day', models.CharField(max_length=10)),
                ('semester_id', models.CharField(blank=True, max_length=10, null=True)),
                ('official_office_in', models.TimeField(blank=True, null=True)),
                ('official_office_out', models.TimeField(blank=True, null=True)),
                ('official_honorarium_time_in', models.TimeField(blank=True, null=True)),
                ('official_honorarium_time_out', models.TimeField(blank=True, null=True)),
                ('official_servicecredit_time_in', models.TimeField(blank=True, null=True)),
                ('official_servicecredit_time_out', models.TimeField(blank=True, null=True)),
                ('official_overtime_time_in', models.TimeField(blank=True, null=True)),
                ('official_overtime_time_out', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='employment_status',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
