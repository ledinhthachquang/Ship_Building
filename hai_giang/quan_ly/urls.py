from django.urls import path
from . import views

urlpatterns = [
    path('', views.trang_chu_quan_ly, name='trang_chu_quan_ly'),
    path('doanh_nghiep/', views.quan_ly_doanh_nghiep, name='quan_ly_doanh_nghiep'),
    path('khach_hang/', views.quan_ly_khach_hang, name='quan_ly_khach_hang'),
]
