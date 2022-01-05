from rest_framework import serializers
from django.conf import settings
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    
    # EmployeeId = serializers.IntegerField()
    EmployeeName = serializers.CharField(max_length=50, default='null')
    EmployeeDepartment =serializers.CharField(max_length=50)
    EmployeeCity = serializers.CharField(max_length=40)

    class Meta:
        model = Employee
        fields = ('__all__')