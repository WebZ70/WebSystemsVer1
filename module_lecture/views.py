from django.shortcuts import render
from .models import *


def page_lecture(request, pk, id_course):
    lecture = Lecture.objects.get(id=pk)
    return render(request, 'module_lecture/page_lecture.html', locals())