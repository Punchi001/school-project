from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone
from django.db.models.enums import Choices
from django.urls import reverse

class MyUserManager(BaseUserManager):
    def create_user(self, regno, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        
        user = self.model(
         
            regno=regno,
         
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, regno,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
        
            regno=regno,
           
            
            password=password,
       
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    
    regno=models.CharField(max_length=15,unique=True)
    
   
    

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'regno'
    
    

    def __str__(self):
        return self.regno

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




class Reporting(models.Model):
    user=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    report=models.BooleanField(max_length=30,default=False)

    def __str__(self):
        return self.user.regno
    def get_absolute_url(self):
        return reverse('home')



class Profile(models.Model):
    
    user=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    email=models.EmailField(default=f'myreg@gmail.com')
    f_name=models.CharField(max_length=30,default='F_NAME')
    l_name=models.CharField(max_length=30,default='M_NAME')
    surname=models.CharField(max_length=30,default='SURNAME')
    pic=models.ImageField(upload_to='profile_pics',default='E:\\IPweb\\media\\profile_pics\\TT.png')
    
    def __str__(self):
        return self.user.regno
    def get_absolute_url(self):
        return reverse('profile')
    
class Schooling(models.Model):
    choices=(('SSAT','SSAT'),('Education','Education'),('HDS','HDS'),('MED','MED'))
    user=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    course=models.CharField(max_length=30)
    school=models.CharField(max_length=30,choices=choices)
    def __str__(self):
        return self.user.regno
    def get_absolute_url(self):
        return reverse('profile')
class Units(models.Model):
    Choices=(('BICT 412','BICT 412'),('STAT 121','STAT 121'),('COMP 202','COMP 202'))
    user=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    unit1=models.CharField(blank=True,choices=Choices,max_length=30)
    unit2=models.CharField(blank=True,choices=Choices,max_length=30)
    unit3=models.CharField(blank=True,choices=Choices,max_length=30)
    unit4=models.CharField(blank=True,choices=Choices,max_length=30)
    unit5=models.CharField(blank=True,choices=Choices,max_length=30)
    approved=models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.regno
    def get_absolute_url(self):
        return reverse('units')
class CName(models.Model):
    course=models.CharField(max_length=30)
    def __str__(self):
        return self.course

class Upload_Units(models.Model):
    unit=models.CharField(max_length=30)
    course=models.ForeignKey(CName,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return str(self.course)
   
