from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            ma_so_thue = form.cleaned_data.get('ma_so_thue')
            password = form.cleaned_data.get('password')
            user = authenticate(ma_so_thue=ma_so_thue, password=password)
            if user is not None:
                login(request, user)
                return redirect('trang_chu_quan_ly')
            else:
                messages.error(request, "Mã số thuế hoặc mật khẩu không đúng.")
    return render(request, 'tai_khoan/dang_nhap.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')