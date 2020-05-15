from course import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(template_name='home.html'), name='home'),
    path('course/', views.Home.as_view(template_name='course/course_user.html'), name='course-user'),
    path('task/<int:id_course>', views.task, name='task'),
    path('lecture/<int:id_course>', views.lecture, name='lecture'),
    path('tests/<int:id_course>', views.tests, name='tests'),
    path('course/<int:pk>/', views.course, name='course'),
    path('course/<int:pk_course>/<str:str_test>/<int:pk_test>', views.test, name='test'),
    path('test/rating', views.test_rating, name='test-rating'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    # path('test-rating/', views.test_rating(), name='test-rating'),


]
