from django.shortcuts import render
from .models import *


def page_task(request, pk, id_course):
    task = Task.objects.get(id=pk)
    return render(request, 'module_task/page_task.html', locals())