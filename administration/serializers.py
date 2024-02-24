# from rest_framework.serializers import Serializer

from rest_framework import serializers
from administration.models import Employees, Products, Departments

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=('product_id', 'product_name','description', 'category', 'sku', 'price', 'created_at', 'image', 'inventory')
                
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')
