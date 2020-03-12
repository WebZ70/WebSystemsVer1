from django.contrib import admin
from .models import *


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


class QuestImageInline(admin.TabularInline):
    model = QuestImage
    extra = 0


class TestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Test._meta.fields]
    inlines = [QuestionInline]

    class Meta:
        model = Test


admin.site.register(Test, TestAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]
    inlines = [AnswerInline, QuestImageInline]

    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Answer._meta.fields]

    class Meta:
        model = Answer


admin.site.register(Answer, AnswerAdmin)


class AnswerStudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AnswerStudent._meta.fields]

    class Meta:
        model = AnswerStudent


admin.site.register(AnswerStudent, AnswerStudentAdmin)


class ResultAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Result._meta.fields]

    class Meta:
        model = Result


admin.site.register(Result, ResultAdmin)


class QuestImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in QuestImage._meta.fields]

    class Meta:
        model = QuestImage


admin.site.register(QuestImage, QuestImageAdmin)