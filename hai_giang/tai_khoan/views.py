from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import DangNhapForm
from .models import NguoiDung

def dang_nhap(request):
    if request.method == 'POST':
        form = DangNhapForm(data=request.POST)
        if form.is_valid():
            ma_so_thue = form.cleaned_data['ma_so_thue']
            mat_khau = form.cleaned_data['password']
            user = authenticate(request, username=ma_so_thue, password=mat_khau)
            if user is not None:
                login(request, user)
                return redirect('')
            else:
                form.add_error(None, 'Mã số thuế hoặc mật khẩu không đúng.')
    else:
        form = DangNhapForm()
    return render(request, 'tai_khoan/dang_nhap.html', {'form': form})

def trang_chu(request):
    return render(request, 'tai_khoan/trang_chu.html')
