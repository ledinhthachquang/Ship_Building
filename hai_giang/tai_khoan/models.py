from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class NguoiDung(AbstractUser):
    ma_so_thue = models.CharField(max_length=20, unique=True)
    
    groups = models.ManyToManyField(Group, related_name='nguoidung_set')
    user_permissions = models.ManyToManyField(Permission, related_name='nguoidung_set')

    def __str__(self):
        return self.username
