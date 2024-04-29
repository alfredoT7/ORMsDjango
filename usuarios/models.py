from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin, UserManager,AbstractUser
    
class UserN(AbstractUser):
    birth_date = models.DateField(null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birth_date']
    email = models.EmailField('email address', unique=True)
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Teacher(UserN):
    teacher_since=models.DateField(null=False)

class Student(UserN):
    matricula_active=models.BooleanField(default=False, null=False)

