from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.fields]

    class Meta:
        model = Task


admin.site.register(Task, TaskAdmin)