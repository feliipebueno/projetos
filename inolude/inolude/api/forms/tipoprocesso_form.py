from django import forms
from api.models import Tbtipoprocesso

class form_tipoprocesso(forms.ModelForm):
    class Meta:
        model = Tbtipoprocesso
        fields = '__all__'
        labels = {
            'de_tipoprocesso': 'Descrição',
            'sg_tipoprocesso': 'Sigla',
        }
