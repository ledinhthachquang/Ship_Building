from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .forms import HoaDonForm, TauForm, KhachHangForm
from .models import HoaDon, KhachHang, Tau, ChiTietHoaDon
from django.db.models import Sum, Q
from datetime import datetime
from weasyprint import HTML
from django.http import HttpResponse, JsonResponse
import locale
from num2words import num2words

locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')

def format_currency(value):
    return locale.format_string("%d", value, grouping=True)

def read_number(value):
    return num2words(value, lang='vi')

def trang_chu(request):
    chi_tiet_hoa_don = ChiTietHoaDon.objects.select_related('hoa_don', 'khach_hang', 'tau').all()
    
    thang = request.GET.get('thang')
    nam = request.GET.get('nam')
    if thang:
        chi_tiet_hoa_don = chi_tiet_hoa_don.filter(hoa_don__ngay_lap__month=int(thang))
    if nam:
        chi_tiet_hoa_don = chi_tiet_hoa_don.filter(hoa_don__ngay_lap__year=int(nam))

    search_query = request.GET.get('search')
    if search_query:
        chi_tiet_hoa_don = chi_tiet_hoa_don.filter(Q(tau__ten_tau__icontains=search_query) | Q(hoa_don__id__icontains=search_query))

    tong_tien = chi_tiet_hoa_don.aggregate(Sum('tau__tien_truoc_thue'))['tau__tien_truoc_thue__sum'] or 0
    tong_thue = chi_tiet_hoa_don.aggregate(Sum('tau__tien_thue'))['tau__tien_thue__sum'] or 0
    tong_thanh_tien = chi_tiet_hoa_don.aggregate(Sum('tau__tien_sau_thue'))['tau__tien_sau_thue__sum'] or 0

    months = range(1, 13)

    formatted_chi_tiet_hoa_don = []
    for chi_tiet in chi_tiet_hoa_don:
        formatted_chi_tiet_hoa_don.append({
            'hoa_don': chi_tiet.hoa_don,
            'khach_hang': chi_tiet.khach_hang,
            'tau': chi_tiet.tau,
            'formatted_tien_truoc_thue': format_currency(chi_tiet.tau.tien_truoc_thue),
            'formatted_tien_thue': format_currency(chi_tiet.tau.tien_thue),
            'formatted_tien_sau_thue': format_currency(chi_tiet.tau.tien_sau_thue),
        })

    return render(request, 'hoa_don/danh_sach_hoa_don.html', {
        'chi_tiet_hoa_don': formatted_chi_tiet_hoa_don,
        'tong_tien': format_currency(tong_tien),
        'tong_thue': format_currency(tong_thue),
        'tong_thanh_tien': format_currency(tong_thanh_tien),
        'tong_thanh_tien_bang_chu': read_number(tong_thanh_tien),
        'thang': thang,
        'nam': nam,
        'months': months,
        'search_query': search_query,
    })

def them_hoa_don(request):
    if request.method == 'POST':
        hoa_don_form = HoaDonForm(request.POST)
        khach_hang_form = KhachHangForm(request.POST)
        tau_choice = request.POST.get('tau_choice')
        
        if tau_choice == 'new':
            tau_form = TauForm(request.POST)
            if hoa_don_form.is_valid() and khach_hang_form.is_valid() and tau_form.is_valid():
                khach_hang = khach_hang_form.save()
                tau = tau_form.save()
                hoa_don = hoa_don_form.save(commit=False)
                hoa_don.khach_hang = khach_hang
                hoa_don.tau = tau
                hoa_don.save()
                
                ChiTietHoaDon.objects.create(
                    hoa_don=hoa_don,
                    khach_hang=khach_hang,
                    tau=tau
                )
                
                return redirect('danh_sach_hoa_don')
        elif tau_choice == 'existing':
            tau_id = request.POST.get('tau_id')
            tau = get_object_or_404(Tau, ma_tau=tau_id)  # Sử dụng ma_tau thay vì id
            if hoa_don_form.is_valid() and khach_hang_form.is_valid():
                khach_hang = khach_hang_form.save()
                hoa_don = hoa_don_form.save(commit=False)
                hoa_don.khach_hang = khach_hang
                hoa_don.tau = tau
                hoa_don.save()
                
                ChiTietHoaDon.objects.create(
                    hoa_don=hoa_don,
                    khach_hang=khach_hang,
                    tau=tau
                )
                
                return redirect('danh_sach_hoa_don')
    else:
        hoa_don_form = HoaDonForm()
        khach_hang_form = KhachHangForm()
        tau_form = TauForm()
        tau_list = Tau.objects.all()
    
    return render(request, 'hoa_don/them_hoa_don.html', {
        'hoa_don_form': hoa_don_form,
        'khach_hang_form': khach_hang_form,
        'tau_form': tau_form,
        'tau_list': tau_list,
    })

def sua_hoa_don(request, id):
    chi_tiet_hoa_don = get_object_or_404(ChiTietHoaDon, id=id)
    if request.method == 'POST':
        hoa_don_form = HoaDonForm(request.POST, instance=chi_tiet_hoa_don.hoa_don)
        tau_form = TauForm(request.POST, instance=chi_tiet_hoa_don.tau)
        khach_hang_form = KhachHangForm(request.POST, instance=chi_tiet_hoa_don.khach_hang)
        if hoa_don_form.is_valid() and tau_form.is_valid() and khach_hang_form.is_valid():
            hoa_don_form.save()
            tau_form.save()
            khach_hang_form.save()
            return redirect('danh_sach_hoa_don')
    else:
        hoa_don_form = HoaDonForm(instance=chi_tiet_hoa_don.hoa_don)
        tau_form = TauForm(instance=chi_tiet_hoa_don.tau)
        khach_hang_form = KhachHangForm(instance=chi_tiet_hoa_don.khach_hang)

    return render(request, 'hoa_don/sua_hoa_don.html', {
        'hoa_don_form': hoa_don_form,
        'tau_form': tau_form,
        'khach_hang_form': khach_hang_form,
        'chi_tiet_hoa_don': chi_tiet_hoa_don,
    })

def xoa_hoa_don(request, id):
    chi_tiet_hoa_don = get_object_or_404(ChiTietHoaDon, id=id)
    if request.method == 'POST':
        chi_tiet_hoa_don.hoa_don.delete()
        chi_tiet_hoa_don.tau.delete()
        chi_tiet_hoa_don.khach_hang.delete()
        chi_tiet_hoa_don.delete()
        
        if ChiTietHoaDon.objects.count() == 0:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='hoa_don';")
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='khach_hang';")
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='tau';")
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='chi_tiet_hoa_don';")
        
        return redirect('danh_sach_hoa_don')
    return render(request, 'hoa_don/xoa_hoa_don.html', {'chi_tiet_hoa_don': chi_tiet_hoa_don})

def in_hoa_don(request, id):
    chi_tiet_hoa_don = get_object_or_404(ChiTietHoaDon, id=id)
    html_string = render_to_string('hoa_don/in_hoa_don.html', {'chi_tiet_hoa_don': chi_tiet_hoa_don})
    html = HTML(string=html_string)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=hoa_don.pdf'
    html.write_pdf(response)
    return response

def get_tau(request, tau_id):
    tau = get_object_or_404(Tau, ma_tau=tau_id)  
    data = {
        'ten_tau': tau.ten_tau,
        'dien_giai': tau.dien_giai,
        'tien_truoc_thue': tau.tien_truoc_thue,
        'thue_suat': tau.thue_suat,
        'tien_thue': tau.tien_thue,
        'tien_sau_thue': tau.tien_sau_thue,
    }
    return JsonResponse(data)
