# forms.py trong app cham_cong
from django import forms
from .models import ChamCong

class ChamCongForm(forms.ModelForm):
    class Meta:
        model = ChamCong
        fields = ['nhan_vien', 'tau', 'ngay_bat_dau', 'ngay_ket_thuc', 'so_ngay_chu_nhat', 'so_ngay_thu_bay']
        widgets = {
            'ngay_bat_dau': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'ngay_ket_thuc': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
