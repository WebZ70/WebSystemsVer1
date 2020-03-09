from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from .models import *
from module_test.models import *
from django.contrib.auth.decorators import login_required
from .permissions import UserPermissionsMixin
from django.http import JsonResponse
import re


class CourseInUser(UserPermissionsMixin, generic.ListView):
    model = Course


class Home(generic.ListView):
    model = Course


class Course():
    model = Course


def test_func(self):
    return Course.objects.filter(userincourse__user_id=self.request.user)


@login_required
def course_user(request):
    courses = UserInCourse.objects.filter(user__userincourse__course_id=request.user.id)
    # if UserInCourse.objects.filter(user__userincourse__course_id=request.user.id):
    #     return redirect('/login/?next=%s' % request.path)
    return render(request, 'course/course_user.html', locals())


def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', locals())


def course(request, pk):
    # course = Course.objects.get(pk=pk)
    tests = TestInCourse.objects.filter(test__testincourse__course_id=pk)
    return render(request, 'course/course.html', locals())


@login_required
def test(request, pk_course, str_test, pk_test):
    session_key = request.session.session_key
    print(request.session.session_key)
    tests = Test.objects.get(pk=pk_test)
    quests = Question.objects.filter(test_id=pk_test)
    # answer = Answer.objects.filter(quest_id=1)
    return render(request, 'course/test.html', locals())


class AnswerStudents(LoginRequiredMixin, generic.ListView):
    model = Answer


def test_rating(request):
    return_dict = dict()
    # session_key = request.session.session_key
    data = request.POST
    datadict = data.dict()
    test_id = data.get("test_id")
    quest_id = 0
    answer_id = 0
    status = 0
    for key in data:
        # if re.findall(r'test_id', key):
        #     print('name_test: ' + datadict.pop(key))
        #     # test_id = datadict.pop(key)
        #     continue

        if re.findall(r'csrfmiddlewaretoken', key):
            print('csrfmiddlewaretoken: ' + datadict.pop(key))
            continue

        if [key] == re.findall(r'\d{1,3}\[key]', key):
            # print('answer_id: ' + datadict.pop(key))
            # print(answer_all.get(id=datadict.pop(key)))
            answer_id = datadict.pop(key)
            continue

        if [key] == re.findall(r'\d{1,3}\[status]', key):
            # print('q_id: ' + datadict.pop(key))
            # print(answer_all.get(id=datadict.pop(key)))
            status = datadict.pop(key)
            continue

        if [key] == re.findall(r'\d{1,3}\[quest]', key):
            quest_id = datadict.pop(key)
            # print('status: ' + datadict.pop(key))

        new_test, created = AnswerStudent.objects.get_or_create(name=request.user, test_id=test_id, quest_id=quest_id,
                                                                answer_id=answer_id)
        # created - False(объект найден) - True(не найден)
        # if not created:
        new_test.status = status
        print(new_test)
        new_test.save(force_update=True)

    total_mark = 0
    # кол-во правильных ответов в тесте
    count_test = Test.objects.get(id=test_id).count_true_answer
    # кортеж всех правильных ответов в тесте
    answer_all = Answer.objects.filter(status=True, quest__test_id=test_id)
    # ответы студента
    answer_student = AnswerStudent.objects.filter(status=True, name=request.user, test_id=test_id)
    # проверка правильности ответов
    for ans in answer_student:
        if ans.answer in answer_all:
            # кол-во правльных ответов
            total_mark += 1
    # добавление результата ответа, если его нет, иначе просто обновляет результат
    result, create = Result.objects.get_or_create(name=request.user, test_id=test_id)
    result.total_mark = total_mark/count_test*100
    result.save(force_update=True)

    return render(request, 'course/select_answer.html', locals())
