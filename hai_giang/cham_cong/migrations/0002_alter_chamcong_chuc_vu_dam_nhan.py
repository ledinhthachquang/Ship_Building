# Generated by Django 5.0.4 on 2024-05-26 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cham_cong', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamcong',
            name='chuc_vu_dam_nhan',
            field=models.IntegerField(choices=[(300000, 'Nhân viên'), (550000, 'Kỹ sư'), (850000, 'Quản đốc')]),
        ),
    ]
