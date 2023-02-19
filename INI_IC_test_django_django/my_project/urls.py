"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




from cgi import test
from tkinter.tix import Select
from turtle import home
from unicodedata import name
from django.contrib import admin
from django.urls import path
from my_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('regisuser/', views.regisuser),
    path('regisuserdata/', views.regisuserdata, name='regisuserdata'),
    path('login/',views.login),
    path('logincheck', views.logincheck, name="logincheck"),
    path('register/',views.register),
    path('regisuserdata/', views.regisuserdata, name='regisuserdata'),
    path('logoff/', views.logoff),
    path('checkbox/',views.checkbox),
    path('header/', views.header),
    path('exam/', views.exam, name="test"),
    path('exam_index/', views.exam_index),
    path('search_exam', views.search_exam, name="search_exam"),
    #path('test/', views.test),
    path('addtest/',views.addtest,name='addtest'),
    path('addthistest',views.addthistest,name='addthistest'),
    path('test/', views.test),
    path('test2/', views.test2),
    path('test3/', views.test3),
    path('exam22/',views.exam22),
    path('cc/',views.cc),
    path('examcfp/',views.examcfp),
    path('testcfp/',views.testcfp),
  
    
    #path('select/',views.SelectView, name='select'),
    #path('home/<int:key>/',views.HomePageView, name='home')
    
    #path('quizz/',views.test, name='Test.id'),
    #path('ajax/random/',views.ajax_random, name='ajax_random')#เพิ่มมา
  
]