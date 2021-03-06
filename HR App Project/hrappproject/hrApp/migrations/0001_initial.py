# Generated by Django 3.0.3 on 2020-03-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDatabaseForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empId', models.IntegerField(max_length=20)),
                ('empName', models.CharField(max_length=20)),
                ('fatherName', models.CharField(max_length=20)),
                ('motherName', models.CharField(max_length=20)),
                ('bloodGroup', models.CharField(max_length=10)),
                ('dateOfBirth', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('maritalStatus', models.CharField(max_length=10)),
                ('spouseName', models.CharField(max_length=10)),
                ('designation', models.CharField(max_length=10)),
                ('emergencyContact', models.IntegerField(max_length=20)),
                ('permanentAdd', models.CharField(max_length=50)),
                ('presentAdd', models.CharField(max_length=50)),
                ('empEmail', models.EmailField(max_length=200)),
                ('empContact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employeedb',
            },
        ),
    ]
