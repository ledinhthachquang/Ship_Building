# Generated by Django 5.0.4 on 2024-05-26 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quan_ly', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tongdoanhthu',
            name='tong_vat_tu',
        ),
        migrations.AddField(
            model_name='tongdoanhthu',
            name='nam',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tongdoanhthu',
            name='thang',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]