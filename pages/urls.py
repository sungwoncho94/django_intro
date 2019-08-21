from django.urls import path
from . import views


urlpatterns = [
    path('num/pull/', views.pullnum),
    path('num/push/', views.pushnum),
    path('static_example/', views.static_example),

    path('lottoinput/', views.lottoinput),
    path('lottoresult/', views.lottoresult),

    path('search/', views.search),
    path('result/', views.result),

    path('lotto/', views.lotto),
    path('isitbirthday/', views.isitbirthday),
    path('student/<str:name>/', views.student),
    path('info/', views.info),
    path('template_language/', views.template_language),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('greeting/<str:name>/', views.greeting),
    path('image/', views.image),
    path('dinner/<str:name>/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
]
