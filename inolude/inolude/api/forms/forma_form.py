from django import forms
from api.models import Tbforma

class form_forma(forms.ModelForm):
    class Meta:
        model = Tbforma
        fields = '__all__'
        labels = {
            'de_forma': 'Descrição',
            'sg_forma': 'Sigla',
        }
