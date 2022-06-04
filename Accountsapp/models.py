from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, user_id, password, **extra_fields):
        if not user_id:
            raise ValueError("The given user_id must be set.")
        user = self.model(
            user_id=user_id,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, **extra_fields):
        user = self.create_user(
            user_id=user_id,
            password=password,
            **extra_fields,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_id = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=128, unique=True)
    phone = models.CharField(max_length=16, unique=True)
    email_auth = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['username', 'email', 'phone']

    class Meta:
        db_table = 'User'
