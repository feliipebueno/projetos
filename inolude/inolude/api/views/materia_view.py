from rest_framework import viewsets
from ..models import Tbmateria
from ..serializers import MateriaSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Tbmateria.objects.all()
    serializer_class = MateriaSerializer