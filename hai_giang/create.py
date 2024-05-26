import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hai_giang.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from tai_khoan.models import NguoiDung

if not NguoiDung.objects.filter(ma_so_thue='0202085694').exists():
    NguoiDung.objects.create(
        ma_so_thue='0202085694',
        password=make_password('1')
    )
    print("Người dùng mặc định đã được tạo.")
else:
    print("Người dùng đã tồn tại.")
