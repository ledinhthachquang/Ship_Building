# vat_tu/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.danh_sach_tau, name='danh_sach_tau'),
    path('them/', views.them_tau, name='them_tau'),
    path('them_vat_tu/', views.them_vat_tu, name='them_vat_tu'),
    path('sua/<int:ma_tau>/', views.sua_tau, name='sua_tau'),
    path('xoa/<int:ma_tau>/', views.xoa_tau, name='xoa_tau'),
    path('sua_vat_tu/<int:id>/', views.sua_vat_tu, name='sua_vat_tu'),
    path('xoa_vat_tu/<int:id>/', views.xoa_vat_tu, name='xoa_vat_tu'),
    path('cap_nhat_thue_suat/<int:ma_tau>/', views.cap_nhat_thue_suat, name='cap_nhat_thue_suat'),
]
