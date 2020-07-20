from rest_framework import viewsets
from ..models import Tbtipoprocesso
from ..serializers import TipoProcessoSerializer

class TipoProcessoViewSet(viewsets.ModelViewSet):
    queryset = Tbtipoprocesso.objects.all()
    serializer_class = TipoProcessoSerializer