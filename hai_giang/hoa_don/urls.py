# hoa_don/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.trang_chu, name='danh_sach_hoa_don'),
    path('them/', views.them_hoa_don, name='them_hoa_don'),
    path('sua/<int:id>/', views.sua_hoa_don, name='sua_hoa_don'),
    path('xoa/<int:id>/', views.xoa_hoa_don, name='xoa_hoa_don'),
    path('in_hoa_don/<int:id>/', views.in_hoa_don, name='in_hoa_don'),
    path('api/get_tau/<int:tau_id>/', views.get_tau, name='get_tau'),

]
