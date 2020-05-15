from module_lecture import views
from django.urls import path

urlpatterns = [
    path('page-lecture/<int:pk>/<int:id_course>', views.page_lecture, name='page_lecture'),
]
