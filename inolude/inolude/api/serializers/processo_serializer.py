from rest_framework import serializers
from api.models import Tbprocesso
from django.core.exceptions import ValidationError

class ProcessoSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, data):
        if data['ar_processo'].size > 10485760:
            raise ValidationError({"ar_processo":"O tamanho maximo do arquivo não pode ser maior que 10MB"})
        return data

    class Meta:
        model = Tbprocesso
        fields ='__all__'