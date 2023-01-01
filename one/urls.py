from django.urls import path

from . import views

urlpatterns = [

    path('register', views.register,name='stdreg'),
    path('home/teacher/', views.home_teacher,name='teahome'),
    path('home/student/', views.home_student,name='stdhome'),
    path('xx',views.cleardata),
    # path('quiz',views.quiz)
    # path('login/',views.login2)
]