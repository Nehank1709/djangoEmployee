from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

# Create your views here.
class EmployeeViews(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response({"status":"success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee)
            return Response({"status":"success", "data": serializer.data}, status=status.HTTP_200_OK)

        employees = Employee.objects.all().order_by('-EmployeeName')
        serializer = EmployeeSerializer(employees, many=True)
        return Response({"status":"success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  
            return Response({"status":"success", "data": serializer.data})
        else:
            return Response({"status":"error", "data": serializer.errors})

    def delete(self, request, id=None):
        employee=get_object_or_404(Employee, id=id)
        employee.delete()
        return Response({"status": "success", "data": "Item deleted"})


    # class EmployeeViews(generics.ListCreateAPIView):
    #     employees = Employee.objects.all()
    #     serializer_class = EmployeeSerializer
    #     name = 'employee-list'

    #     filter_fields = (
    #         'EmployeeDepartment',
    #         'EmployeeCity',
    #     )