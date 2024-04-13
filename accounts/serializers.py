# from rest_framework.serializers import Serializer

from accounts.models import Employees, Products, Departments

#Auth
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import User

#Auth
class TokenObtainPairWithEmailSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data

    default_error_messages = {
        'no_active_account': 'No active account found with the given credentials'
    }

    email = serializers.EmailField()

    def validate_email(self, value):
        user = User.objects.filter(email=value).first()

        if not user:
            raise serializers.ValidationError(self.default_error_messages['no_active_account'])

        if not user.is_active:
            raise serializers.ValidationError(self.default_error_messages['no_active_account'])

        return value

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def get_token(self, user):
        return RefreshToken.for_user(user)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('full_name', 'company_name', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            full_name=validated_data['full_name'],
            company_name=validated_data['company_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user

class TokenObtainPairWithEmailSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data

    default_error_messages = {
        'no_active_account': 'No active account found with the given credentials'
    }

    email = serializers.EmailField()

    def validate_email(self, value):
        user = User.objects.filter(email=value).first()

        if not user:
            raise serializers.ValidationError(self.default_error_messages['no_active_account'])

        if not user.is_active:
            raise serializers.ValidationError(self.default_error_messages['no_active_account'])

        return value

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def get_token(self, user):
        return RefreshToken.for_user(user)
# Auth: End
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','Image')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=('product_id', 'product_name','description', 'category', 'sku', 'price', 'created_at', 'image', 'inventory')
                
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')
