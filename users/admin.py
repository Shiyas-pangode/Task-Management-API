from django.contrib import admin
from .models import CustomUser

class CustomModelAdmin(admin.ModelAdmin):
    list_display = ('role',)
admin.site.register(CustomUser ,CustomModelAdmin)
