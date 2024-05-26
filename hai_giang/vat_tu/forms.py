from django import forms
from .models import Tau, VatTu

class TauForm(forms.ModelForm):
    class Meta:
        model = Tau
        fields = ['ten_tau', 'dien_giai']


class VatTuForm(forms.ModelForm):
    class Meta:
        model = VatTu
        fields = ['ten_vat_tu', 'khoi_luong', 'don_gia', 'he_so_cong', 'tau']
        widgets = {
            'he_so_cong': forms.Select(choices=[(1.00, '1.00'), (2.00, '2.00'), (3.00, '3.00')]),
        }

