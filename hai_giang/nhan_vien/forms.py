from django import forms
from .models import NhanVien

class NhanVienForm(forms.ModelForm):
    class Meta:
        model = NhanVien
        fields = ['ma_nhan_vien', 'ten_nhan_vien', 'que_quan', 'so_cccd', 'dia_chi_thuong_tru', 'chuc_vu']
        widgets = {
            'chuc_vu': forms.Select(choices=[('Nhan vien', 'Nhân viên'), ('Ky su', 'Kỹ sư'), ('Quan doc', 'Quản đốc')])
        }
