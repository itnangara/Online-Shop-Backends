from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Employees, Departments
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .forms import MyUserCreationForm, MyUserChangeForm

class MyUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_staff',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, MyUserAdmin)


admin.site.register(Employees)
admin.site.register(Departments)
