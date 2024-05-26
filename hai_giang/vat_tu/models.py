# vat_tu/models.py

from django.db import models
from hoa_don.models import Tau

class VatTu(models.Model):
    ten_vat_tu = models.CharField(max_length=100)
    khoi_luong = models.DecimalField(max_digits=12, decimal_places=2)
    don_gia = models.DecimalField(max_digits=12, decimal_places=2)
    he_so_cong = models.DecimalField(max_digits=4, decimal_places=2, choices=[(1.00, '1.00'), (2.00, '2.00'), (3.00, '3.00')])
    tau = models.ForeignKey(Tau, related_name='vattu', on_delete=models.CASCADE)
    
    @property
    def tien_vat_tu(self):
        return self.khoi_luong * self.don_gia * self.he_so_cong

class QuyetToanVatTu(models.Model):
    vat_tu = models.ForeignKey(VatTu, on_delete=models.CASCADE)
    tau = models.ForeignKey(Tau, on_delete=models.CASCADE)
    thanh_tien = models.DecimalField(max_digits=12, decimal_places=2)

