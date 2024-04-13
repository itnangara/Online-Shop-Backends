from django.urls import path
from accounts import views

# from rest_framework.urlpatterns import format_suffix_patterns

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('employees', views.employeeApi),
    path('employees/<int:id>', views.employeeApi),
    path('employees/savefile',views.SaveFile),

    path('products', views.productApi),
    path('products/<int:id>', views.productApi),

    path('departments', views.departmentApi),
    path('departments/<int:id>', views.departmentApi),   

    path('products/savefile',views.SaveFile),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)