from django.shortcuts import render, redirect, get_object_or_404
from .models import NhanVien
from .forms import NhanVienForm

def danh_sach_nhan_vien(request):
    if request.method == 'POST':
        form = NhanVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_nhan_vien')
    else:
        form = NhanVienForm()

    nhan_vien_list = NhanVien.objects.all()
    return render(request, 'nhan_vien/danh_sach_nhan_vien.html', {'form': form, 'nhan_vien_list': nhan_vien_list})

def sua_nhan_vien(request, ma_nhan_vien):
    nhan_vien = get_object_or_404(NhanVien, ma_nhan_vien=ma_nhan_vien)
    if request.method == 'POST':
        form = NhanVienForm(request.POST, instance=nhan_vien)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_nhan_vien')
    else:
        form = NhanVienForm(instance=nhan_vien)
    return render(request, 'nhan_vien/sua_nhan_vien.html', {'form': form, 'nhan_vien': nhan_vien})

def xoa_nhan_vien(request, ma_nhan_vien):
    nhan_vien = get_object_or_404(NhanVien, ma_nhan_vien=ma_nhan_vien)
    if request.method == 'POST':
        nhan_vien.delete()
        return redirect('danh_sach_nhan_vien')
    return render(request, 'nhan_vien/xoa_nhan_vien.html', {'nhan_vien': nhan_vien})