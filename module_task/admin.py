from django.contrib import admin
from .models import *


class FileTask(admin.TabularInline):
    model = FileTask
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.fields]
    inlines = [FileTask]

    class Meta:
        model = Task


admin.site.register(Task, TaskAdmin)