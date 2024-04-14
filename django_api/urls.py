from django.contrib import admin
from django.urls import path
from django.conf.urls import include

#Auth
from accounts.views import RegisterView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    
    #Auth
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('rest_registration.api.urls')),
    
    #path('api/v1/', include(api_urlpatterns)),

    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]

#Auth
# REST_REGISTRATION = {
#     'REGISTER_VERIFICATION_ENABLED': False,
#     'REGISTER_EMAIL_VERIFICATION_ENABLED': False,
#     'RESET_PASSWORD_VERIFICATION_ENABLED': False,
# }
