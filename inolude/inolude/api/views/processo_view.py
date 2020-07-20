from rest_framework import viewsets
from ..models import Tbprocesso
from ..serializers import ProcessoSerializer

class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Tbprocesso.objects.all()
    serializer_class = ProcessoSerializer