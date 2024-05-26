from django.urls import path
from .views import dang_nhap, trang_chu

urlpatterns = [
    path('dang_nhap/', dang_nhap, name='dang_nhap'),
]
