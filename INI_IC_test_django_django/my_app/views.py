from functools import reduce
from imghdr import tests
from os import name
import pkgutil
import select
from turtle import shearfactor
from unittest import result
from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from my_app.models import Test
from my_app.models import quizz
from my_app.models import quizzcfp4
from django.db import connection
from django.core.exceptions import PermissionDenied


import my_app
from .models import *

from django.core.paginator import Paginator

from django.http import JsonResponse
import random


# Create your views here.

def index(request):
    biology = ['fname', 'lname', 'age', 'gender', '...']
    mydata = {
        "biology" : biology 
    }
    return render(request, 'my_app/index.html', mydata)

def regisuser(request):
    return render(request, 'my_app/regisuser.html')


def login(request):
    print("login")
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'my_app/login.html')

def logincheck(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    print("kuy")
    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.error(request, "ไม่พบข้อมูลในระบบ")
        return  redirect('/login')


def register(request):
    return render(request, 'my_app/register.html')



def regisuserdata(request):
   
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    gender = request.POST['gender']
    birthday = request.POST['birthday']
    print(gender)
    print(type(gender))
   
   

    if password == repassword:
        if User.objects.filter(username=username).exists():
            return HttpResponse("User ซ้ำในระบบ")
        elif User.objects.filter(email=email).exists():
            return HttpResponse("email ซ้ำในระบบ")

       
        
        else:
            # user = User.objects.create_user(
            #     first_name = fname,
            #     last_name = lname,
            #     username=username,
            #     password=password,
            #     email=email
            # )
            # user.save()

            newuser = User() 
            newuser.username = username
            newuser.email = email
            newuser.first_name = fname
            newuser.last_name = lname
            newuser.set_password(password)
            newuser.save()

            newprofile = Profile()
            newprofile.user = User.objects.get(username=username)
            newprofile.Birthday = birthday
            newprofile.Gender = gender
            print(newprofile.Gender)
            newprofile.save()

            return redirect('/login')
        
    else:
        messages.error(request, "Password and Repasssword ไม่ตรงกัน")
        return redirect("/register")





def checkbox(request):
    return render(request, 'my_app/checkbox.html')


def header(request):
    return render(request, "my_app/header.html")

def logoff(request):
    auth.logout(request)
    return redirect("/login")


def exam(request):
    allexam = Test.objects.all()
    exam_per_page = 9
    paginator = Paginator(allexam, exam_per_page)
    page = request.GET.get('page') 

    # คิวรี่ group
    group = []
    for index,exam in enumerate(allexam): 
        group.append(exam.Test_Topice)
    group = list(set(group))


    allexam = paginator.get_page(page)
    # print('COUNT : ' ,len(allexam))
    context = {'allexam':allexam}

    # แยกแถวละ 3 
    allrow = []
    row = []
    
    for index,exam in enumerate(allexam):
        
        if index%3 == 0 :
            if index != 0 :
                allrow.append(row)
            row = []
            row.append(exam)
        else :
            row.append(exam)

    allrow.append(row)


    context['allrow'] = allrow
    context['group'] = group
    

    # print(context)
    return render(request, 'my_app/exam.html',context)
    

def search_exam(request):
    
    
    
    

    if request.method == "POST":
        # allexam = Test.objects.all()
        allexam = Test.objects.all()
        # คิวรี่ group
        group = []
        for index,exam in enumerate(allexam): 
            group.append(exam.Test_Topice)
        group = list(set(group))

        searched = request.POST['searched']

        # ค้นด้วย ชื่อ หรือ หมวด
        cat = ''
        try: cat = request.POST['cat']
        except : pass
        if cat == 'babo' :  allexam = Test.objects.filter(Test_Topice__contains=searched)
        else:allexam = Test.objects.filter(Test_Name__contains=searched)
        

        exam_per_page = 9
        paginator = Paginator(allexam, exam_per_page)
        page = request.GET.get('page') 
        allexam = paginator.get_page(page)
        # print('COUNT : ' ,len(allexam))
        context = {'allexam':allexam}

        # แยกแถวละ 3 
        allrow = []
        row = []
        for index,exam in enumerate(allexam):
            if index%3 == 0 :
                if index != 0 :
                    allrow.append(row)
                row = []
                row.append(exam)
            else :
                row.append(exam)

        allrow.append(row)
        context['allrow'] = allrow
        context['group'] = group
    return render(request, 'my_app/exam.html',context)    

#def ajax_random(request):
    #if request.is_ajax():
        #r = random.randint(100, 1000)
        #return JsonResponse({'num' :r})
    #else:
        #return render(request, 'my_app/exam.html')
        

def test(request):
    results=quizz.objects.filter()
    
      
    # Test = models.ForeignKey(Test,on_delete=CASCADE)

    for star in results.iterator():
        print(star)

    # print(results)
    # print("BOBA")
    return render(request,'my_app/index2.html',{"quizz":results}) 

def test2(request):
    results=quizz.objects.filter(Test=6)
    #Test = models.ForeignKey(Test,on_delete=CASCADE)

    #for star in results.iterator():
        #print(star)

     #print(results)
     #print("BOBA")
    return render(request,'my_app/index2.html',{"quizz":results}) 
def test3(request):
    results=quizz.objects.filter(Test=3)
    #Test = models.ForeignKey(Test,on_delete=CASCADE)

    #for star in results.iterator():
        #print(star)

     #print(results)
     #print("BOBA")
    return render(request,'my_app/index2.html',{"quizz":results}) 


def addtest(request):
    return render(request, 'my_app/addtest.html')

def addthistest(request):
    Test_Name = request.POST['Test_Name']
    Test_Topice = request.POST['Test_Topice']
    user = request.user.is_superuser
    if request.user.is_superuser == True:
        user =  request.user
        print(request.user)
        newtest = Test()
        newtest.user = user
        newtest.Test_Name = Test_Name
        newtest.Test_Topice = Test_Topice
        newtest.save()
    else : return  redirect('/login')


    # print(Test_Name,Test_Topice)

    return  redirect('/addtest')

def exam_index(request):
      
    return render(request,'my_app/exam_index.html') 

def exam22(request):
    
    return render(request, 'my_app/cfp or ic.html')

def cc(request):
    
    return render(request, 'my_app/cer777.html')

def examcfp(request):
    allexam = Testcfp4.objects.all()
    exam_per_page = 9
    paginator = Paginator(allexam, exam_per_page)
    page = request.GET.get('page') 

    # คิวรี่ group
    group = []
    for index,exam in enumerate(allexam): 
        group.append(exam.Test_Topice)
    group = list(set(group))


    allexam = paginator.get_page(page)
    # print('COUNT : ' ,len(allexam))
    context = {'allexam':allexam}

    # แยกแถวละ 3 
    allrow = []
    row = []
    
    for index,exam in enumerate(allexam):
        
        if index%3 == 0 :
            if index != 0 :
                allrow.append(row)
            row = []
            row.append(exam)
        else :
            row.append(exam)

    allrow.append(row)


    context['allrow'] = allrow
    context['group'] = group
    

    # print(context)
    return render(request, 'my_app/examcfp.html',context)

def testcfp(request):
    results=quizzcfp4.objects.filter()
    #Test = models.ForeignKey(Test,on_delete=CASCADE)

    #for star in results.iterator():
        #print(star)

     #print(results)
     #print("BOBA")
    return render(request,'my_app/index4.html',{"quizzcfp4":results}) 

#uncle
# def Register(request):

#     context = {}

#     if request.method=='POST':
#         data = request.POST.copy()
#         fullname = data.get('fullname')
#         username = data.get('username')
#         mobile = data.get('mobile')
#         password = data.get('password')
#         password2 = data.get('password2')
#         local = data.get('local')

#         context['warning'] = 'กรอกรหัสผ่านให้ตรงกัน'
#         if password != password2:
#             return render(request,'company/register.html',context)
#         try :
#             check = User.objects.get(username=username)
#         except :
           
#             newuser = User() 
#             newuser.username = username
#             newuser.email = username
#             newuser.first_name = fullname
#             newuser.set_password(password)
#             newuser.save()


#             newprofile = Profile()
#             newprofile.user = User.objects.get(username=username)
#             newprofile.mobile = mobile
#             newprofile.locals = local
#             newprofile.save()

#         if username == ''and password =="":
#             context['message'] = 'กรอกข้อมูลด้วย'
#             return render(request,'company/register.html',context)

#         try: 
#             user = authenticate(username=username,password=password)
#             login(request,user)

#         except:            
#             context['message'] = 'username หรือ password ผิด'  
        


#         context['message'] = 'register สำเร็จ'
#     return render(request,'company/register.html',context)