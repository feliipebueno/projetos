from django import forms
from api.models import Tbprocesso,Tbtipoprocesso,Tbmateria,Tbforma

class TipoProcessoChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.de_tipoprocesso

class MateriaChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.de_tipomateria

class formaChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.de_forma

class form_processo(forms.ModelForm):
    cod_tipoprocesso = TipoProcessoChoiceField(Tbtipoprocesso.objects.all(),empty_label="Selecione uma opção")
    cod_materia = MateriaChoiceField(Tbmateria.objects.all(),empty_label="Selecione uma opção")
    cod_forma = formaChoiceField(Tbforma.objects.all(),empty_label="Selecione uma opção")
    class Meta:
        model = Tbprocesso
        fields = '__all__'
        labels = {
            'nu_processo': 'Numero',
            'dt_processo': 'Data do Processo',
            'ar_processo': 'Arquivo',
            'vl_processo': 'Valor',
            'cod_tipoprocesso': 'Tipo do Processo',
            'cod_materia': 'Materia',
            'cod_forma': 'Forma',
        }