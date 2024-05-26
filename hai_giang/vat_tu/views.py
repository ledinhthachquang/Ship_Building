from django.shortcuts import render, get_object_or_404, redirect
from .models import Tau, VatTu
from .forms import TauForm, VatTuForm

def danh_sach_tau(request):
    form = VatTuForm()
    tau_list = Tau.objects.prefetch_related('vattu').all()
    return render(request, 'vat_tu/danh_sach_tau.html', {'tau_list': tau_list, 'form': form})

def them_tau(request):
    if request.method == 'POST':
        form = TauForm(request.POST)
        if form.is_valid():
            tau = form.save(commit=False)
            tau.tien_truoc_thue = 0
            tau.tien_thue = 0
            tau.tien_sau_thue = 0
            tau.save()
            return redirect('danh_sach_tau')
    else:
        form = TauForm()
    return render(request, 'vat_tu/them_tau.html', {'form': form})

def them_vat_tu(request):
    if request.method == 'POST':
        form = VatTuForm(request.POST)
        if form.is_valid():
            vat_tu = form.save(commit=False)
            vat_tu.tau = form.cleaned_data['tau']
            tien_vat_tu = vat_tu.khoi_luong * vat_tu.don_gia * vat_tu.he_so_cong
            vat_tu.save()

            tau = vat_tu.tau
            tau.tien_truoc_thue += tien_vat_tu
            tau.tien_thue = tau.tien_truoc_thue * (tau.thue_suat / 100)
            tau.tien_sau_thue = tau.tien_truoc_thue + tau.tien_thue
            tau.save()
        return redirect('danh_sach_tau')
    else:
        form = VatTuForm()
    return render(request, 'vat_tu/them_vat_tu.html', {'form': form})

def sua_tau(request, ma_tau):
    tau = get_object_or_404(Tau, pk=ma_tau)
    if request.method == 'POST':
        form = TauForm(request.POST, instance=tau)                            
        if form.is_valid():
            form.save()
            return redirect('danh_sach_tau')
    else:
        form = TauForm(instance=tau)
    return render(request, 'vat_tu/sua_tau.html', {'form': form, 'tau': tau})

def xoa_tau(request, ma_tau):
    tau = get_object_or_404(Tau, pk=ma_tau)
    if request.method == 'POST':
        tau.delete()
        return redirect('danh_sach_tau')
    return render(request, 'vat_tu/xoa_tau.html', {'tau': tau})

def sua_vat_tu(request, id):
    vat_tu = get_object_or_404(VatTu, pk=id)
    tau = vat_tu.tau
    if request.method == 'POST':
        form = VatTuForm(request.POST, instance=vat_tu)
        if form.is_valid():
            old_tien_vat_tu = vat_tu.tien_vat_tu

            vat_tu = form.save(commit=False)
            vat_tu.tau = tau  # Đảm bảo gán đúng tàu
            vat_tu.save()

            new_tien_vat_tu = vat_tu.khoi_luong * vat_tu.don_gia * vat_tu.he_so_cong

            # Thêm thông báo gỡ lỗi
            print("Old tien_vat_tu: ", old_tien_vat_tu)
            print("New tien_vat_tu: ", new_tien_vat_tu)
            print("Old tien_truoc_thue: ", tau.tien_truoc_thue)

            # Tính lại các giá trị của tàu
            tau.tien_truoc_thue = sum(vt.tien_vat_tu for vt in tau.vattu.all())
            print("Updated tien_truoc_thue: ", tau.tien_truoc_thue)

            tau.tien_thue = tau.tien_truoc_thue * (tau.thue_suat / 100)
            tau.tien_sau_thue = tau.tien_truoc_thue + tau.tien_thue
            tau.save()

            # Thêm thông báo gỡ lỗi sau khi lưu
            print("Updated tau: ", tau.tien_truoc_thue, tau.tien_thue, tau.tien_sau_thue)

            return redirect('danh_sach_tau')
    else:
        form = VatTuForm(instance=vat_tu)
    return render(request, 'vat_tu/sua_vat_tu.html', {'form': form, 'vat_tu': vat_tu})


def xoa_vat_tu(request, id):
    vat_tu = get_object_or_404(VatTu, pk=id)
    tau = vat_tu.tau
    if request.method == 'POST':
        tau.tien_truoc_thue -= vat_tu.tien_vat_tu
        tau.tien_thue = tau.tien_truoc_thue * (tau.thue_suat / 100)
        tau.tien_sau_thue = tau.tien_truoc_thue + tau.tien_thue
        tau.save()
        vat_tu.delete()
        return redirect('danh_sach_tau')
    return render(request, 'vat_tu/xoa_vat_tu.html', {'vat_tu': vat_tu})



def cap_nhat_thue_suat(request, ma_tau):
    tau = get_object_or_404(Tau, pk=ma_tau)
    if request.method == 'POST':
        thue_suat = request.POST.get('thue_suat')
        tau.thue_suat = float(thue_suat)
        tau.tien_thue = tau.tien_truoc_thue * (tau.thue_suat / 100)
        tau.tien_sau_thue = tau.tien_truoc_thue + tau.tien_thue
        tau.save()
        return redirect('danh_sach_tau')
    return redirect('danh_sach_tau')
