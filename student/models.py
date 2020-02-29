from django.db import models
from course.models import Course, Test, TestInCourse
from django.db.models.signals import post_save
from django.dispatch import receiver
from module_test.models import *
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return "%s" % self.user

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    # def save(self, *args, **kwargs):
    #     self.user = User.objects.get(self.user)
    #     self.user.save()


class StudentInCourse(models.Model):
    course = models.ForeignKey(Course, blank=True, null=True, default=None, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, blank=True, null=True, default=None, on_delete=models.CASCADE)

    mark_test = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    mark_task = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    mark_to_course = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return "%s" % self.student.name

    class Meta:
        verbose_name = "Стдент"
        verbose_name_plural = "Студент"

    def save(self, *args, **kwargs):
        self.mark_to_course = self.mark_task + self.mark_test
        # student = self.student.id
        # student_in_test = StudentInTest.objects.filter(student_id=student)
        # create_std_test = StudentInTest.objects.create()
        # create_std_test = student_in_test
        # create_std_test.save(force_update=True)
        super(StudentInCourse, self).save(*args, **kwargs)


# class StudentInTest(models.Model):
#     student = models.ForeignKey(Student, blank=True, null=True, default=None, on_delete=models.CASCADE)
#     test = models.ForeignKey(Test, blank=True, null=True, default=None, on_delete=models.CASCADE)
#
#     created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
#
#     def __str__(self):
#         return "%s" % self.test
#
#     class Meta:
#         verbose_name = "Тестов у студента"
#         verbose_name_plural = "Тестов у студентов"
#
#     def save(self, *args, **kwargs):
#         # student_in_course = self.student_in_course.course_id
#         # test = self.test
#         student = self.student
#         # student.course.objects.filter(test=self.test)
#         # error!!!
#         test = TestInCourse.objects.filter(course__studentincourse__student_id=student.id).select_related('test').values_list('test__name_test', flat=True)
#         print(test.values('test__name_test'))
#         t = set()
#         for item in test:
#             t.add(item)
#
#         self.test_name = t
#         # self.test = t
#         # self.test.save(force_insert=True)
#         super(StudentInTest, self).save(*args, **kwargs)


class AnswerTestStudent(models.Model):
    student = models.ForeignKey(StudentInCourse, blank=True, null=True, default=None, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, blank=True, null=True, default=None, on_delete=models.CASCADE)
    mark_test = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    def __str__(self):
        return "%s" % self.student.student.name

    class Meta:
        verbose_name = "Ответ стдента"
        verbose_name_plural = "Ответы студента"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.old_mark = self.mark_test
        if self.test is not None:
            self.old_name_test = self.test.name_test
        else:
            self.old_name_test = None

    def save(self, *args, **kwargs):
        student = self.student.student_id
        test_student = Test.objects.get(pk=self.test_id)

        # --> template 'test_student'
        tmp = 'student_answer_' + test_student.name_test + '_student_' + str(student)

        if test_student.name_test.startswith('student_answer_'):
            super(AnswerTestStudent, self).save(update_fields=['mark_test'], **kwargs)
            return 0

        all_test = Test.objects.all().values_list('name_test', flat=True)
        if tmp in all_test:
            return 0
        else:
            if self.old_name_test is not None:
                if self.old_name_test != test_student.name_test:
                    return 0
            test_student.name_test = tmp
            test_student.pk = None

        self.test = test_student
        self.test.save()

        super(AnswerTestStudent, self).save(*args, **kwargs)
