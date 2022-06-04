from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

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

class Lane(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    damage = models.IntegerField()
    images = models.ImageField(blank=True, upload_to="images", null=True)

    class Meta:
        db_table = 'Lane'

class Building(Lane, models.Model):
    lane_id = models.ForeignKey("Lane", related_name="lane", on_delete=models.CASCADE, db_column="lane_id")
    city = models.CharField(max_length=32)  # 시
    county = models.CharField(max_length=32)  # 군
    district = models.CharField(max_length=32)  # 구
    road_address = models.CharField(max_length=64)  # 도로명주소
    
    class Meta:
        db_table = 'Building'

class Scrap(models.Model):
    scrap_id = models.AutoField(primary_key=True)
    lane_id = models.ForeignKey('Lane', on_delete=models.CASCADE, db_column='lane_id')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')

    class Meta:
        db_table = 'Scrap'
        managed = False

