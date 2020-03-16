from django.db import models

# Create your models here.
class Employee(models.Model):
    empId = models.CharField(max_length=20)
    empName = models.CharField(max_length=20)
    empEmail = models.EmailField(max_length=200)
    empContact = models.CharField(max_length=15)

    class Meta:
        db_table = 'employeeApp'
