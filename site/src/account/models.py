from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class MyAccountManger(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have email address")
        if not username:
            raise ValueError("user must have usrname")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
            username = username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)
        return user




class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    username = models.CharField(verbose_name="username", max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = MyAccountManger()

    def __str__(self):
        return self.email

    def has_parm(self, parm, obj = None):
        return self.is_admin

    def has_module_parms(self,app_label):
        return True        