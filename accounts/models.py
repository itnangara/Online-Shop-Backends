from django.db import models
from django.utils import timezone

# Auth
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, first_name, last_name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('date_joined', default=timezone.now)
        return self.create_user(first_name, last_name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    #username = models.CharField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    @property
    def is_admin(self):
        return self.is_staff

    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    REQUIRED_FIELDS = ['last_name']


    def __str__(self):
        return self.email


    def get_first_name(self):
        return self.first_name


    def get_short_name(self):
        return self.first_name.split(' ')[0]
# Auth: End

# Other models
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    Image = models.CharField(max_length=500)

class Products(models.Model):
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