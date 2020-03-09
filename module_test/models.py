from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# from student.models import Student


class Test(models.Model):
    name_test = models.CharField(max_length=48)
    count_true_answer = models.DecimalField(max_digits=1, decimal_places=0, default=0)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return "%s" % self.name_test

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class Question(models.Model):
    test = models.ForeignKey(Test, blank=True, null=True, default=None, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=256)

    def __str__(self):
        return "%s" % self.question_text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    answer_text = models.CharField(max_length=256)
    quest = models.ForeignKey(Question, blank=True, null=True, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    # def save(self, *args, **kwargs):
    #     quest = Test.objects.get(id=self.quest.test.id)
    #     if self.status:
    #         quest.count_true_answer += 1
    #     quest.save(force_update=True)
    #
    #     super(Answer, self).save(*args, **kwargs)


def answer_post_save(sender, instance, created, **kwargs):
    # quest = Question.objects.filter(test_id=instance.quest.test.id)
    answer = Answer.objects.filter(status=True, quest__test_id=instance.quest.test.id).count()
    instance.quest.test.count_true_answer = answer
    instance.quest.test.save(force_update=True)


post_save.connect(answer_post_save, sender=Answer)


class AnswerStudent(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    test = models.ForeignKey(Test, blank=True, null=True, default=None, on_delete=models.CASCADE)
    quest = models.ForeignKey(Question, blank=True, null=True, default=None, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, blank=True, null=True, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(null=False, blank=False, default=False)
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)

    def __str__(self):
        return self.name.username

    class Meta:
        verbose_name = "Ответ студента"
        verbose_name_plural = "Ответы студентов"


class Result(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    test = models.ForeignKey(Test, blank=True, null=True, default=None, on_delete=models.CASCADE)
    total_mark = models.DecimalField(max_digits=3, decimal_places=0, default=2)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.name.username

    class Meta:
        verbose_name = "Результаты теста"
        verbose_name_plural = "Результаты тестов"
