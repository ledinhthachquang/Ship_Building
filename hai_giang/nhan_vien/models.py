from django.db import models

from django.db import models

class NhanVien(models.Model):
    ma_nhan_vien = models.AutoField(primary_key=True)
    ten_nhan_vien = models.CharField(max_length=100)
    que_quan = models.CharField(max_length=100)
    so_cccd = models.CharField(max_length=12)
    dia_chi_thuong_tru = models.CharField(max_length=200)
    chuc_vu = models.CharField(max_length=100, choices=[
        ('Nhân viên', 'Nhân viên'),
        ('Kỹ sư', 'Kỹ sư'),
        ('Quản đốc', 'Quản đốc')
    ])

    def __str__(self):
        return self.ten_nhan_vien