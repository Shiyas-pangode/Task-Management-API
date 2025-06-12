from django.contrib import admin
from .models import EmployeeModel

class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ()
admin.site.register(EmployeeModel ,EmployeeModelAdmin)
