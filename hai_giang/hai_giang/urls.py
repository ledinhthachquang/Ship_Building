"""
URL configuration for hai_giang project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tai_khoan/', include('tai_khoan.urls')),
    path('hoa_don/', include('hoa_don.urls')),
    path('nhan_vien/', include('nhan_vien.urls')),
    path('cham_cong/', include('cham_cong.urls')),
    path('vat_tu/', include('vat_tu.urls')),
    path('', include('quan_ly.urls')),
    path('dang_nhap/', lambda request: redirect('tai_khoan:login')),
]