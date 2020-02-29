from module_test import views
from django.urls import path

urlpatterns = [
    path('test/', views.main, name='course.html'),
]
