from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tai_khoan/', include('tai_khoan.urls')),
    path('', include('quan_ly.urls')),
    path('hoa_don/', include('hoa_don.urls')),
    path('nhan_vien/', include('nhan_vien.urls')),
    path('cham_cong/', include('cham_cong.urls')),
    path('vat_tu/', include('vat_tu.urls')),
]
