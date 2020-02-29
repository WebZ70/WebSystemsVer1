from django.contrib import admin
from .models import *


# class StudentInTestInline(admin.TabularInline):
#     model = StudentInTest
#     extra = 0


class StudentInCourseInline(admin.TabularInline):
    model = StudentInCourse
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]
    inlines = [StudentInCourseInline]

    class Meta:
        model = Student


admin.site.register(Student, StudentAdmin)


class AnswerTestStudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AnswerTestStudent._meta.fields]

    class Meta:
        model = AnswerTestStudent


admin.site.register(AnswerTestStudent, AnswerTestStudentAdmin)


# class StudentInTestAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in StudentInTest._meta.fields]
#
#     class Meta:
#         model = StudentInTest
#
#
# admin.site.register(StudentInTest, StudentInTestAdmin)
