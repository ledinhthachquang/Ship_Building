from django.db import models

class HoaDon(models.Model):
    ngay_lap = models.DateTimeField()
    ma_tien_te = models.CharField(max_length=3, choices=[('VND', 'VND'), ('USD', 'USD')])
    hinh_thuc_thanh_toan = models.CharField(max_length=20, choices=[('Tiền mặt', 'Tiền mặt'), ('Chuyển khoản', 'Chuyển khoản')])
    email_nguoi_ban = models.EmailField(blank=True, null=True)
    sdt_nguoi_ban = models.CharField(max_length=15, blank=True, null=True)
    stk_nguoi_ban = models.CharField(max_length=20, blank=True, null=True)
    nh_nguoi_ban = models.CharField(max_length=50, blank=True, null=True)

class Tau(models.Model):
    ma_tau = models.AutoField(primary_key=True)
    ten_tau = models.CharField(max_length=100)
    dien_giai = models.TextField()
    tien_truoc_thue = models.DecimalField(max_digits=12, decimal_places=2)
    thue_suat = models.DecimalField(max_digits=4, decimal_places=2, choices=[(8.00, '8%'), (10.00, '10%')], default=8.00)
    tien_thue = models.DecimalField(max_digits=12, decimal_places=2)
    tien_sau_thue = models.DecimalField(max_digits=12, decimal_places=2)

class KhachHang(models.Model):
    ten_cong_ty = models.CharField(max_length=100)
    ma_so_thue = models.CharField(max_length=20)
    dia_chi = models.CharField(max_length=200)
    sdt = models.CharField(max_length=15)

class ChiTietHoaDon(models.Model):
    hoa_don = models.ForeignKey(HoaDon, on_delete=models.CASCADE)
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    tau = models.ForeignKey(Tau, on_delete=models.CASCADE)
