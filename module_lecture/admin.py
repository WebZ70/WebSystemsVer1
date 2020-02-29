from django.contrib import admin
from .models import *


class LectureAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Lecture._meta.fields]

    class Meta:
        model = Lecture


admin.site.register(Lecture, LectureAdmin)