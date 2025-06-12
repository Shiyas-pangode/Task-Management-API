from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('api.v1.user.urls')),
    path('api/auth/',include('api.v1.auth.urls')),
    path('api/taskmanager/',include('api.v1.taskmanager.urls')),
    path('api/employee/',include('api.v1.employee.urls')),

]
