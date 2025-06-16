from django.contrib import admin
from .models import TaskModel

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('title','description','status')
admin.site.register(TaskModel ,TaskModelAdmin)
