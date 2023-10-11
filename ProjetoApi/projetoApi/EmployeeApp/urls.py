from django.urls import path
from EmployeeApp import views

urlpatterns = [
    path('department', views.DepartmentList.as_view()),
    path('department/<int:pk>' ,views.DepartmentList.as_view()),
    path('employee/<int:pk>', views.EmployeeList.as_view()),
    path('employee', views.EmployeeCreate.as_view()),
    path('department_add/', views.DepartmentCreate.as_view()),
    path("department_edit/<int:pk>", views.DepartmentDetail.as_view()),
    path("employee_edit/<int:pk>", views.EmployeeDetail.as_view())
]
