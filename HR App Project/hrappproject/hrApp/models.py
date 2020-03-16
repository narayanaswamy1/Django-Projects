from django.db import models

# Create your models here.
class EmployeeDatabaseForm(models.Model):

    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        )

    marital_status = (
    ('Married', 'Married'),
    ('Widowed', 'Widowed'),
    ('Separated','Separated'),
    ('Divorced', 'Divorced'),
    ('Single', 'Single'),
    )

    empId = models.IntegerField()
    empName = models.CharField(max_length=20)
    fatherName = models.CharField(max_length=20)
    motherName = models.CharField(max_length=20)
    bloodGroup = models.CharField(max_length=20)
    dateOfBirth = models.DateField(auto_now_add=False)
    sex = models.CharField(max_length=6, choices=gender_choices)
    maritalStatus = models.CharField(max_length=10, choices=marital_status, default='Single')
    spouseName = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    emergencyContact = models.IntegerField()
    permanentAdd = models.CharField(max_length=50)
    presentAdd = models.CharField(max_length=50)
    empEmail = models.EmailField(max_length=200)
    empContact = models.CharField(max_length=20)

    class Meta:
        db_table = 'employeedb'
