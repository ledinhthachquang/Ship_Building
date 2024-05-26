# hoa_don/admin.py

from django.contrib import admin
from .models import HoaDon, KhachHang, Tau, ChiTietHoaDon

class HoaDonAdmin(admin.ModelAdmin):
    list_display = ('id', 'ngay_lap', 'hinh_thuc_thanh_toan')
    search_fields = ('id', 'hinh_thuc_thanh_toan')

class KhachHangAdmin(admin.ModelAdmin):
    list_display = ('id', 'ten_cong_ty', 'ma_so_thue')
    search_fields = ('ten_cong_ty', 'ma_so_thue')

class ChiTietHoaDonAdmin(admin.ModelAdmin):
    list_display = ('hoa_don', 'khach_hang', 'tau')
    search_fields = ('hoa_don__id', 'khach_hang__ten_cong_ty', 'tau__ten_tau')

admin.site.register(HoaDon, HoaDonAdmin)
admin.site.register(KhachHang, KhachHangAdmin)
admin.site.register(ChiTietHoaDon, ChiTietHoaDonAdmin)
