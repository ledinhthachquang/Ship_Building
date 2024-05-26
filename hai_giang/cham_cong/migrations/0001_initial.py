# Generated by Django 5.0.4 on 2024-05-26 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hoa_don', '0001_initial'),
        ('nhan_vien', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChamCong',
            fields=[
                ('ma_cham_cong', models.AutoField(primary_key=True, serialize=False)),
                ('ngay_bat_dau', models.DateTimeField()),
                ('ngay_ket_thuc', models.DateTimeField()),
                ('tong_cong', models.IntegerField()),
                ('chuc_vu_dam_nhan', models.IntegerField()),
                ('so_gio_lam_viec', models.IntegerField()),
                ('nhan_vien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nhan_vien.nhanvien')),
                ('tau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoa_don.tau')),
            ],
        ),
    ]