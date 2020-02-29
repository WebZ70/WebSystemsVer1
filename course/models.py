from django.db import models
from django.contrib.auth.models import User
from module_test.models import Test
from module_task.models import Task
from module_lecture.models import Lecture


# from student.models import Student


class Course(models.Model):
    name_course = models.CharField(max_length=48)
    description = models.CharField(max_length=256, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    # students = models.ManyToManyField(User, related_name='students', blank=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return "%s" % self.name_course

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def is_user_course(self):
        if self.students is None:
            return False
        else:
            return True


class TestInCourse(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True, default=None, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, blank=True, null=True, default=None, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return "%s" % self.test.name_test

    class Meta:
        verbose_name = "Тест в курсе"
        verbose_name_plural = "Тестов в курсе"


class TaskInCourse(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True, default=None, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, blank=True, null=True, default=None, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return "%s" % self.task.name_task

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class LectureInCourse(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True, default=None, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, blank=True, null=True, default=None, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return "%s" % self.lecture.name_lecture

    class Meta:
        verbose_name = "Лекция"
        verbose_name_plural = "Лекции"


class UserInCourse(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True, default=None, on_delete=models.CASCADE)
    students = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return "%s" % self.user.username

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def is_user_course(self):
        if self.user is None:
            return False
        else:
            return True
