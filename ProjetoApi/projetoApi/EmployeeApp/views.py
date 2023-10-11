from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView, Response, status
from django.http.response import JsonResponse
from EmployeeApp.models import Departments,Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer
from rest_framework import generics

class EmployeeCreate(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
          queryset = Employee.objects.all()
          return queryset
    
class DepartmentList(generics.ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    
class EmployeeList(generics.RetrieveAPIView):
 
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
   
    
class DepartmentCreate(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    
    def get_queryset(self):
          queryset = Departments.objects.all()
          return queryset
    
class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = DepartmentSerializer
    queryset = Departments.objects.all()
    
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    
