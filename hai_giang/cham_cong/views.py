from django.shortcuts import render, redirect, get_object_or_404
from .models import ChamCong
from nhan_vien.models import NhanVien
from hoa_don.models import Tau
from .forms import ChamCongForm
from datetime import datetime

def danh_sach_cham_cong(request):
    nhan_vien_list = NhanVien.objects.all()
    cham_cong_list = ChamCong.objects.select_related('nhan_vien', 'tau').all()

    for nhan_vien in nhan_vien_list:
        cham_congs = cham_cong_list.filter(nhan_vien=nhan_vien)
        tong_luong = 0
        for cham_cong in cham_congs:
            so_cong = (cham_cong.ngay_ket_thuc - cham_cong.ngay_bat_dau).days - cham_cong.so_ngay_chu_nhat - cham_cong.so_ngay_thu_bay
            so_cong += cham_cong.so_ngay_chu_nhat * 1.5 + cham_cong.so_ngay_thu_bay * 1.5
            if cham_cong.nhan_vien.chuc_vu == 'Nhân viên':
                luong = so_cong * 300000
            elif cham_cong.nhan_vien.chuc_vu == 'Kỹ sư':
                luong = so_cong * 550000
            else:  # Quản đốc
                luong = so_cong * 850000
            tong_luong += luong
        nhan_vien.tong_luong = tong_luong

    if request.method == 'POST':
        form = ChamCongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_cham_cong')
    else:
        form = ChamCongForm()

    return render(request, 'cham_cong/danh_sach_cham_cong.html', {
        'nhan_vien_list': nhan_vien_list,
        'cham_cong_list': cham_cong_list,
        'form': form
    })

def sua_cham_cong(request, id):
    cham_cong = get_object_or_404(ChamCong, ma_cham_cong=id)
    if request.method == 'POST':
        form = ChamCongForm(request.POST, instance=cham_cong)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_cham_cong')
    else:
        form = ChamCongForm(instance=cham_cong)
    return render(request, 'cham_cong/sua_cham_cong.html', {'form': form})

def xoa_cham_cong(request, id):
    cham_cong = get_object_or_404(ChamCong, ma_cham_cong=id)
    cham_cong.delete()
    return redirect('danh_sach_cham_cong')
