from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    ma_so_thue = forms.CharField(label="Mã số thuế", max_length=15)
    password = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        ma_so_thue = cleaned_data.get("ma_so_thue")
        password = cleaned_data.get("password")

        if ma_so_thue and password:
            user = authenticate(ma_so_thue=ma_so_thue, password=password)
            if user is None:
                raise forms.ValidationError("Mã số thuế hoặc mật khẩu không đúng.")
        return cleaned_data
