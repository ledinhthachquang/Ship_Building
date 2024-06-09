from django.shortcuts import render
from django.db.models import Sum, F, DecimalField
from decimal import Decimal
from cham_cong.models import ChamCong
from hoa_don.models import HoaDon, ChiTietHoaDon
from django.contrib.auth.decorators import login_required
import locale
from num2words import num2words

locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')

def format_currency(value):
    return locale.format_string("%d", value, grouping=True)

def read_number(value):
    return num2words(value, lang='vi')


def tinh_doanh_thu(hoa_don_list):
    tong_thu_tu_hoa_don = hoa_don_list.aggregate(Sum('chitiethoadon__tau__tien_sau_thue'))['chitiethoadon__tau__tien_sau_thue__sum'] or Decimal(0)

    cham_cong_list = ChamCong.objects.filter(tau__in=hoa_don_list.values_list('chitiethoadon__tau', flat=True))
    tong_luong_nhan_vien = Decimal(0)

    for cham_cong in cham_cong_list:
        so_cong = (cham_cong.ngay_ket_thuc - cham_cong.ngay_bat_dau).days - cham_cong.so_ngay_chu_nhat - cham_cong.so_ngay_thu_bay
        so_cong += cham_cong.so_ngay_chu_nhat * Decimal(1.5) + cham_cong.so_ngay_thu_bay * Decimal(1.5)
        if cham_cong.nhan_vien.chuc_vu == 'Nhân viên':
            luong = so_cong * Decimal(300000)
        elif cham_cong.nhan_vien.chuc_vu == 'Kỹ sư':
            luong = so_cong * Decimal(550000)
        else:  # Quản đốc
            luong = so_cong * Decimal(850000)
        tong_luong_nhan_vien += luong

    tong_doanh_thu = tong_thu_tu_hoa_don - tong_luong_nhan_vien

    return tong_thu_tu_hoa_don, tong_luong_nhan_vien, tong_doanh_thu

@login_required
def trang_chu_quan_ly(request):
    hoa_don_list = HoaDon.objects.all()

    thang = request.GET.get('thang')
    nam = request.GET.get('nam')
    if thang:
        hoa_don_list = hoa_don_list.filter(ngay_lap__month=int(thang))
    if nam:
        hoa_don_list = hoa_don_list.filter(ngay_lap__year=int(nam))

    hoa_don_data = []
    for hoa_don in hoa_don_list:
        chi_tiet_hoa_don_list = ChiTietHoaDon.objects.filter(hoa_don=hoa_don)
        tong_tien = chi_tiet_hoa_don_list.aggregate(
            tong_tien=Sum('tau__tien_truoc_thue', output_field=DecimalField())
        )['tong_tien'] or Decimal(0)
        tien_thue = chi_tiet_hoa_don_list.aggregate(
            tien_thue=Sum('tau__tien_thue', output_field=DecimalField())
        )['tien_thue'] or Decimal(0)
        tien_sau_thue = chi_tiet_hoa_don_list.aggregate(
            tien_sau_thue=Sum('tau__tien_sau_thue', output_field=DecimalField())
        )['tien_sau_thue'] or Decimal(0)

        chi_phi_luong = Decimal(0)
        for chi_tiet in chi_tiet_hoa_don_list:
            cham_cong_list = ChamCong.objects.filter(tau=chi_tiet.tau)
            for cham_cong in cham_cong_list:
                so_cong = (cham_cong.ngay_ket_thuc - cham_cong.ngay_bat_dau).days - cham_cong.so_ngay_chu_nhat - cham_cong.so_ngay_thu_bay
                so_cong += cham_cong.so_ngay_chu_nhat * Decimal(1.5) + cham_cong.so_ngay_thu_bay * Decimal(1.5)
                if cham_cong.nhan_vien.chuc_vu == 'Nhân viên':
                    luong = so_cong * Decimal(300000)
                elif cham_cong.nhan_vien.chuc_vu == 'Kỹ sư':
                    luong = so_cong * Decimal(550000)
                else:  # Quản đốc
                    luong = so_cong * Decimal(850000)
                chi_phi_luong += luong

        doanh_thu = tien_sau_thue - chi_phi_luong

        hoa_don_data.append({
            'hoa_don': hoa_don,
            'tong_tien': tong_tien,
            'tien_thue': tien_thue,
            'tien_sau_thue': tien_sau_thue,
            'chi_phi_luong': chi_phi_luong,
            'doanh_thu': doanh_thu,
            'formatted_tong_tien': format_currency(tong_tien),
            'formatted_tien_thue': format_currency(tien_thue),
            'formatted_tien_sau_thue': format_currency(tien_sau_thue),
            'formatted_chi_phi_luong': format_currency(chi_phi_luong),
            'formatted_doanh_thu': format_currency(doanh_thu),
            'read_doanh_thu': read_number(doanh_thu)
        })

    tong_thu_tu_hoa_don, tong_luong_nhan_vien, tong_doanh_thu = tinh_doanh_thu(hoa_don_list)
    months = range(1, 13)

    return render(request, 'quan_ly/trang_chu.html', {
        'hoa_don_data': hoa_don_data,
        'tong_thu_tu_hoa_don': format_currency(tong_thu_tu_hoa_don),
        'tong_luong_nhan_vien': format_currency(tong_luong_nhan_vien),
        'tong_doanh_thu': format_currency(tong_doanh_thu),
        'read_tong_doanh_thu': read_number(tong_doanh_thu),
        'thang': thang,
        'nam': nam,
        'months': months,
    })




def quan_ly_doanh_nghiep(request):
    return render(request, 'quan_ly/quan_ly_doanh_nghiep.html')

def quan_ly_khach_hang(request):
    return render(request, 'quan_ly/quan_ly_khach_hang.html')
