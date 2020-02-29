from django.contrib import admin
from .models import *
# from student.admin import StudentInCourseInline


class UserInCourseInline(admin.TabularInline):
    model = UserInCourse
    extra = 0


class TestsInCourseInline(admin.TabularInline):
    model = TestInCourse
    extra = 0


class TaskInCourseInline(admin.TabularInline):
    model = TaskInCourse
    extra = 0


class LectureInCourseInline(admin.TabularInline):
    model = LectureInCourse
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Course._meta.fields]
    inlines = [TestsInCourseInline, TaskInCourseInline, LectureInCourseInline, UserInCourseInline]

    class Meta:
        model = Course


admin.site.register(Course, CourseAdmin)


class TestInCourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TestInCourse._meta.fields]

    class Meta:
        model = TestInCourse


admin.site.register(TestInCourse, TestInCourseAdmin)
#
#
# class TaskInCourseAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in TaskInCourse._meta.fields]
#
#     class Meta:
#         model = TaskInCourse
#
#
# admin.site.register(TaskInCourse, TaskInCourseAdmin)
#
#
# class LectureInCourseAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in LectureInCourse._meta.fields]
#
#     class Meta:
#         model = LectureInCourse
#
#
# admin.site.register(LectureInCourse, LectureInCourseAdmin)