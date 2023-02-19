from pydoc import ttypager
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *



class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','Test_Name',"Test_Topice",'Tests_id']

class Questions(admin.ModelAdmin):
    list_display = ['id', 'Question_Name','Question_No','Test_id']

class Choices(admin.ModelAdmin):
    list_display = ['id','Choice_No','Choice_Name','Choice_TrueFalse','Question_ID_id']

class Answers(admin.ModelAdmin):
    list_display = ['id','Answer_Point','Choice_id']

class Profiles(admin.ModelAdmin):
    list_display = ['id','Gender','Birthday','user_id']


class superTests(admin.ModelAdmin):
    list_display = ['id','Gender','user_id']

class quizzs(admin.ModelAdmin):
    list_display = ['id','quiz_number','Question','option1','option2','option3','option4','corrans','Test_id',]

class Testcfp4s(admin.ModelAdmin):
    list_display = ['id', 'user','Test_Name',"Test_Topice",'Testcfp4_id']

class quizzcfp4s(admin.ModelAdmin):
    list_display = ['id','quiz_number','Question','option1','option2','option3','option4','corrans','Testcfp4']


admin.site.register(Test,TaskAdmin)
admin.site.register(Question,Questions)
admin.site.register(Choice,Choices)
admin.site.register(Answer,Answers)
admin.site.register(Profile,Profiles)
admin.site.register(superTest,superTests)
admin.site.register(quizz,quizzs)
admin.site.register(Testcfp4,Testcfp4s)
admin.site.register(quizzcfp4,quizzcfp4s)
