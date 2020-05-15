from module_task import views
from django.urls import path

urlpatterns = [
    path('page-task/<int:pk>/<int:id_course>', views.page_task, name='page_task'),
]
