from django.db import models

class TongDoanhThu(models.Model):
    thang = models.IntegerField(null=True, blank=True)
    nam = models.IntegerField(null=True, blank=True)
    tong_thu_tu_hoa_don = models.DecimalField(max_digits=12, decimal_places=2)
    tong_luong_nhan_vien = models.DecimalField(max_digits=12, decimal_places=2)
    tong_doanh_thu = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return f'Doanh thu {self.thang}/{self.nam} - {self.tong_doanh_thu}'
