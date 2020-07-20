from rest_framework import serializers
from api.models import Tbmateria

class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbmateria
        fields ='__all__'