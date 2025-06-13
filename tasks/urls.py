from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/',include('api.v1.user.urls')),
    path('api/v1/auth/',include('api.v1.auth.urls')),
    path('api/v1/taskmanager/',include('api.v1.taskmanager.urls')),
    path('api/v1/employee/',include('api.v1.employee.urls')),

]
