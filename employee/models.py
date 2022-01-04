from django.db import models
from django.conf import settings

# Create your models here.
class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=50, blank=True, null=True)
    EmployeeDepartment =models.CharField(max_length=50, blank=True, null=True)
    EmployeeAge = models.IntegerField(blank=True, null=True)
    EmployeePhone = models.CharField(max_length=20, blank=True, null=True)
    EmployeeEmail = models.CharField(max_length=40, blank=True, null=True)
    EmployeeCity = models.CharField(max_length=40, blank=True, null=True)
    EmployeeSalary = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return str(self.EmployeeId) + str(self.EmployeeName)