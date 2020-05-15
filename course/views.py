from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from .models import *
from module_test.models import *
from django.contrib.auth.decorators import login_required
from .permissions import UserPermissionsMixin
import re
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


class CourseInUser(UserPermissionsMixin, generic.ListView):
    model = Course


class Home(generic.ListView):
    model = Course


def task(request, id_course):
    # this_course = Course.objects.get(id=pk)
    tasks = TaskInCourse.objects.filter(task__taskincourse__course_id=id_course)
    return render(request, 'module_task/tasks.html', locals())


def tests(request, id_course):
    # this_course = Course.objects.get(id=pk)
    tests = TestInCourse.objects.filter(test__testincourse__course_id=id_course)
    return render(request, 'module_test/tests.html', locals())


def lecture(request, id_course):
    # this_course = Course.objects.get(id=pk)
    lectures = LectureInCourse.objects.filter(lecture__lectureincourse__course_id=id_course)
    return render(request, 'module_lecture/lectures.html', locals())


def base(request, pk):
    id_course = pk

    return render(request, 'base_materials.html', locals())


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
    id_course = pk
    print(id_course)
    tests = TestInCourse.objects.filter(test__testincourse__course_id=pk)
    tasks = TaskInCourse.objects.filter(task__taskincourse__course_id=pk)
    return render(request, 'module_lecture/lectures.html', locals())


@login_required
def test(request, pk_course, str_test, pk_test):
    session_key = request.session.session_key
    tests = Test.objects.get(pk=pk_test)
    quests = Question.objects.filter(test_id=pk_test)
    quest_image = QuestImage.objects.filter(quest__test_id=pk_test)
    # answer_image = AnswerImage.objects.filter(answer__quest__test_id=pk_test)
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
            # print('csrfmiddlewaretoken: ' + datadict.pop(key))
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
        # new_test.result
        # print(new_test)
        new_test.save(force_update=True)

    # блок начисления баллов
    total_mark = 0
    mark = 0
    # кол-во вопросов
    count_quests = Question.objects.filter(test_id=test_id).count()
    # кортеж всех ответов в тесте
    answer_all = Answer.objects.filter(quest__test_id=test_id)
    # ответы студента
    answer_student = AnswerStudent.objects.filter(status=True, name=request.user, test_id=test_id)

    # проверка правильности ответов
    old_id = 0
    for ans in answer_student.select_related('quest'):
        quest_id = ans.quest.id
        if old_id == quest_id:
            continue

        count_aqs = AnswerStudent.objects.filter(name=request.user, quest_id=quest_id, status=True)
        count_aq = Answer.objects.filter(quest_id=quest_id, status=True)
        if count_aqs.count() != count_aq.count():
            continue

        for item in count_aqs:
            if item.answer in count_aq:
                mark += 1

        if count_aq.count() == mark:
            # print("Ответ правильный: "+str(quest_id))
            total_mark += 1
        old_id = quest_id
        mark = 0
    print(total_mark)
    print(total_mark/count_quests*100)
    # конец блока начисления ответов
    # добавление результата ответа, если его нет, иначе просто обновляет результат
    result, create = Result.objects.get_or_create(name=request.user, test_id=test_id)
    result.total_mark = total_mark/count_quests*100
    result.save(force_update=True)

    return render(request, 'course/select_answer.html', locals())


# registration views
class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
