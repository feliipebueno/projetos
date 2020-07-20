from rest_framework import serializers
from api.models import Tbtipoprocesso

class TipoProcessoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbtipoprocesso
        fields ='__all__'
        labels = {
            'de_tipoprocesso': 'Tipo de Processo', 'sg_tipoprocesso': 'Sigla',
        }