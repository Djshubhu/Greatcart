from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class MyAccManager(BaseUserManager):
    def create_user(self,username,last_name,first_name,email,password=None):

        if not email:
            return ValueError('Email is Complusory') 

        if not first_name:
            return ValueError('First_name is Complusory') 

        if not username:
            return ValueError('Username is Complusory') 

        user =self.model(
            email =       self.normalize_email(email),
            username    = username,
            last_name   = last_name,
            first_name  = first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,last_name,first_name,email,password):
        user =self.create_user(
            email =       self.normalize_email(email),
            username    = username,
            last_name   = last_name ,
            first_name  = first_name,
            password=password,

        )
        user.is_admin    =    True
        user.is_staff    =    True
        user.is_active    =   True
        user.is_superuser   =  True
        user.save(using=self._db)
        return user



class Accounts(AbstractBaseUser):
    first_name =        models.CharField(max_length=50)
    last_name =         models.CharField(max_length=50)
    username =          models.CharField(max_length=50, unique=True)
    email =             models.EmailField(unique=True)
    phone=              models.CharField(max_length=12)

    #   Required

    joined_date =     models.DateTimeField(auto_now_add=True)
    last_login =      models.DateTimeField(auto_now_add=True)
    is_admin   =      models.BooleanField(default=False)
    is_staff   =      models.BooleanField(default=False)
    is_active  =      models.BooleanField(default=False)
    is_superadmin  =  models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= 'username','last_name','first_name'


    object = MyAccManager()
    class Meta:
        verbose_name        = 'Account'
        verbose_name_plural = 'Accounts'


    def __str__(self):
        return self.email

    
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True