from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import NguoiDung
from django.contrib.auth import authenticate

class DangNhapForm(AuthenticationForm):
    ten_cong_ty = forms.ChoiceField(
        choices=[('CÔNG TY TNHH ĐẦU TƯ PHÁT TRIỂN THƯƠNG MẠI HẢI GIANG', 'CÔNG TY TNHH ĐẦU TƯ PHÁT TRIỂN THƯƠNG MẠI HẢI GIANG')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    ma_so_thue = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mã số thuế'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mật khẩu'})
    )

    class Meta:
        model = NguoiDung
        fields = ('ten_cong_ty', 'ma_so_thue', 'password')

    def clean(self):
        cleaned_data = super().clean()
        ma_so_thue = cleaned_data.get('ma_so_thue')
        password = cleaned_data.get('password')
        
        if ma_so_thue and password:
            try:
                user = NguoiDung.objects.get(ma_so_thue = ma_so_thue)
                if not user.check_password(password):
                    raise forms.ValidationError("Mật khẩu không đúng .")
            except NguoiDung.DoesNotExist:
                raise forms.ValidationError("Mã số thuế không đúng")
        return cleaned_data