from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)




class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
    
        )
        user.is_admin = True
      
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = True 
    is_student = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

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


class Department(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
    # student = models.ManyToManyField(Student)



    class Score(models.Model):
        test_name = models.CharField(max_length=10,default='hell')
        test_score = models.IntegerField()

    


class Test(models.Model):
    text = models.CharField(max_length=20,default='hell')
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)

class Question(models.Model):
        test = models.ForeignKey(Test,on_delete=models.CASCADE)
        text = models.CharField(max_length=10,default='hell')

class Choice(models.Model):
        c_text = models.CharField(max_length=10,default='hell ')
        is_ans = models.BooleanField(default=False)






    


