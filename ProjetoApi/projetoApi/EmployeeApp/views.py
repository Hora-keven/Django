from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView, Response, status
from django.http.response import JsonResponse
from EmployeeApp.models import Departments,Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from rest_framework import generics
class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class DepartmensList(generics.ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    
class MetodoAPI(APIView):
    def get(self, request):
        items = ["Keven"]
        response = {"Datas": items}
        return Response(response, status=status.HTTP_200_OK)

@csrf_exempt
def departmentApi(request, id):
    if request.method == 'GET':
        departments = Departments.objects.filter(DepartmentId__icontains=id)
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('ADDED SUCESSFULLY', safe=False)
        return JsonResponse('Failed to add', safe=False)
    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer = departments_serializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("UPDATE SUCCESSFULLY", safe=False)
        return JsonResponse('Failed to update')
    
    elif request.method == 'DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse('DELETE SUCCESSFULLY', safe=False)
    return JsonResponse('FAILED TO DELETE')



@csrf_exempt
def employeeApi(request, id):
    if request.method == 'GET':
        employees = Employee.objects.filter(EmployeeId__icontains=id)
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employeee_serializer=EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('ADDED SUCESSFULLY', safe=False)
        return JsonResponse('Failed to add', safe=False)
    
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = employee_serializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("UPDATE SUCCESSFULLY", safe=False)
        return JsonResponse('Failed to update')
    
    elif request.method == 'DELETE':
        employee=Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse('DELETE SUCCESSFULLY', safe=False)
    return JsonResponse('FAILED TO DELETE')