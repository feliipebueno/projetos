from rest_framework import serializers
from api.models import Tbforma

class FormaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbforma
        fields ='__all__'