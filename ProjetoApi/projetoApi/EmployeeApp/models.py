from django.db import models

from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.DepartmentName

class Employee(models.Model):
   EmployeeId = models.AutoField(primary_key=True)
   EmployeeName = models.CharField(max_length=500)
   Department = models.CharField(max_length=500)
   DateOfJoining = models.DateField()
   PhotoFileName = models.CharField(max_length=500)
   
   def __str__(self) -> str:
      return self.EmployeeName



    

