from django.contrib import admin

# Register your models here.
from softuni_python_web_basics.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
