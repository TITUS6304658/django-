import random
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Test(models.Model):
    # user one to may
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Tests_id= models.CharField(max_length= 100,default="")
    Test_Name = models.CharField(max_length= 100)
    Test_Topice = models.CharField(max_length= 100)

    ##def __str__(self):
        ##return f"{self.Test_Name}-{self.Test_Topice}"

    ##def get_questions(self):
        ##quizz = list(self.quizz_set.all())
        ##random.shuffle(quizz)
        ##return quizz[:self.number_of_questions]
  
class Question(models.Model):
    # Test_ID
    Test = models.ForeignKey(Test,on_delete=CASCADE)
    Question_Name = models.CharField(max_length= 500)
    Question_No = models.CharField(max_length= 500)
    def __str__(self):
        return self.question 

class Choice(models.Model):
    Question_ID = models.ForeignKey(Question,on_delete=CASCADE)
    Choice_No = models.CharField(max_length=500)
    Choice_Name = models.CharField(max_length=500)
    Choice_TrueFalse = models.BooleanField(default=False)


class Answer(models.Model):
    Choice = models.ForeignKey(Choice,on_delete=CASCADE)
    Answer_Point =  models.BooleanField(default=False)
    # w8 for Result_ID

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Gender = models.CharField(max_length=100)
    Birthday = models.DateField()

class superTest(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Gender = models.CharField(max_length=100)


class newtable(models.Model):
    numba = models.CharField(max_length=100)
    omega = models.DecimalField(max_digits=65,decimal_places=10)


class quizz(models.Model):
    Test = models.ForeignKey(Test,on_delete=CASCADE)
    quiz_number=models.CharField(max_length=100)
    Question=models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    corrans=models.CharField(max_length=100)
    #class meta:
        #db_table="my_app_test"
    #def __str__(self):
       #return self


class Testcfp4(models.Model):
    # user one to may
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Testcfp4_id= models.CharField(max_length= 100,default="")
    Test_Name = models.CharField(max_length= 100)
    Test_Topice = models.CharField(max_length= 100)
  

class quizzcfp4(models.Model):
    Testcfp4= models.ForeignKey(Testcfp4,on_delete=CASCADE)
    quiz_number=models.CharField(max_length=100)
    Question=models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    corrans=models.CharField(max_length=100)