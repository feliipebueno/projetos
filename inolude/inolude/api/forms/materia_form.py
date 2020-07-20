from django import forms
from api.models import Tbmateria

class form_materia(forms.ModelForm):
    class Meta:
        model = Tbmateria
        fields = '__all__'
        labels = {
            'de_tipomateria': 'Descrição',
            'sg_tipomateria': 'Sigla',
        }