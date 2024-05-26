from django.db import models
from nhan_vien.models import NhanVien
from hoa_don.models import Tau

class ChamCong(models.Model):
    ma_cham_cong = models.AutoField(primary_key=True)
    nhan_vien = models.ForeignKey(NhanVien, on_delete=models.CASCADE)
    tau = models.ForeignKey(Tau, on_delete=models.CASCADE)
    ngay_bat_dau = models.DateTimeField()
    ngay_ket_thuc = models.DateTimeField()
    so_ngay_chu_nhat = models.IntegerField()
    so_ngay_thu_bay = models.IntegerField()
    so_gio_lam_viec = models.IntegerField(editable=False, default=0)
    tong_cong = models.IntegerField(editable=False, default=0)
    luong = models.DecimalField(max_digits=12, decimal_places=2, editable=False, default=0)

    def save(self, *args, **kwargs):
        so_cong = (self.ngay_ket_thuc - self.ngay_bat_dau).days - self.so_ngay_chu_nhat - self.so_ngay_thu_bay
        so_cong += self.so_ngay_chu_nhat * 1.5 + self.so_ngay_thu_bay * 1.5
        self.tong_cong = so_cong
        self.so_gio_lam_viec = so_cong * 8
        if self.nhan_vien.chuc_vu == 'Nhân viên':
            self.luong = so_cong * 300000
        elif self.nhan_vien.chuc_vu == 'Kỹ sư':
            self.luong = so_cong * 550000
        else:  # Quản đốc
            self.luong = so_cong * 850000
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nhan_vien} - {self.tau}'
