from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/', include('taskapi.urls')),
    path('user/',include('api.v1.user.urls')),
    path('auth/',include('api.v1.auth.urls')),
    path('taskapi/',include('api.v1.tasks.urls')),
    path('employee/',include('api.v1.employee.urls'))

]
