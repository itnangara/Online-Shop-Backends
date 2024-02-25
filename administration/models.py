from django.db import models

# Create your models here.

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    Image = models.CharField(max_length=500)

class Products(models.Model):
    # Defining fields for the Products table
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    sku = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField()
    image = models.CharField(max_length=500)
    inventory = models.IntegerField(default=0)

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)


class Roles(models.Model):  
    ADMIN = 'admin'
    USERS = 'users'

    STATUS_CHOICES = (  
        (ADMIN, 'System Administrators'),
        (USERS, 'Staff')
    )

    work_description = models.CharField(max_length=255)  
    work_status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default=USERS)