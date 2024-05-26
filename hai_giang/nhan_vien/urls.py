# nhan_vien/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.danh_sach_nhan_vien, name='danh_sach_nhan_vien'),
    path('sua/<int:ma_nhan_vien>/', views.sua_nhan_vien, name='sua_nhan_vien'),
    path('xoa/<int:ma_nhan_vien>/', views.xoa_nhan_vien, name='xoa_nhan_vien'),
]
