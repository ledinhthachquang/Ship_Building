from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, ma_so_thue, password=None, **extra_fields):
        if not ma_so_thue:
            raise ValueError('The Mã số thuế must be set')
        user = self.model(ma_so_thue=ma_so_thue, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, ma_so_thue, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(ma_so_thue, password, **extra_fields)

class NguoiDung(AbstractBaseUser, PermissionsMixin):
    ma_so_thue = models.CharField(max_length=15, unique=True)
    ten_cong_ty = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'ma_so_thue'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.ma_so_thue
