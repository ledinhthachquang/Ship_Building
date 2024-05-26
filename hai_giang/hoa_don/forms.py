from django import forms
from .models import HoaDon, Tau, KhachHang

class HoaDonForm(forms.ModelForm):
    class Meta:
        model = HoaDon
        fields = [
            'ngay_lap',
            'ma_tien_te',
            'hinh_thuc_thanh_toan',
            'email_nguoi_ban',
            'sdt_nguoi_ban',
            'stk_nguoi_ban',
            'nh_nguoi_ban',
        ]
        widgets = {
            'ngay_lap': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'ma_tien_te': forms.Select(choices=[('VND', 'VND'), ('USD', 'USD')]),
            'hinh_thuc_thanh_toan': forms.Select(choices=[('Tiền mặt', 'Tiền mặt'), ('Chuyển khoản', 'Chuyển khoản')]),
        }

class TauForm(forms.ModelForm):
    class Meta:
        model = Tau
        fields = [
            'ten_tau',
            'dien_giai',
            'tien_truoc_thue',
            'thue_suat',
            'tien_thue',
            'tien_sau_thue',
        ]
        widgets = {
            'thue_suat': forms.Select(choices=[(8.00, '8%'), (10.00, '10%')]),
        }

class KhachHangForm(forms.ModelForm):
    class Meta:
        model = KhachHang
        fields = [
            'ten_cong_ty',
            'ma_so_thue',
            'dia_chi',
            'sdt',
        ]
