from django.urls import path
from EmployeeApp import views

urlpatterns = [
    path('department', views.DepartmensList.as_view()),
    path('department/<int:id>' ,views.departmentApi),
    path('employee/<int:id>', views.employeeApi),
    path('employee', views.EmployeeList.as_view()),
    path('teste', views.MetodoAPI.as_view())
]
