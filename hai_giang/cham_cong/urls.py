from django.urls import path
from . import views

urlpatterns = [
    path('', views.danh_sach_cham_cong, name='danh_sach_cham_cong'),
    path('sua/<int:id>/', views.sua_cham_cong, name='sua_cham_cong'),
    path('xoa/<int:id>/', views.xoa_cham_cong, name='xoa_cham_cong'),
]
