from django.contrib import admin
from .models import *


class FileLecture(admin.TabularInline):
    model = FileLecture
    extra = 0


class LectureAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Lecture._meta.fields]
    inlines = [FileLecture]

    class Meta:
        model = Lecture


admin.site.register(Lecture, LectureAdmin)