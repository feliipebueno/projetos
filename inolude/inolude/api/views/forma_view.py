from rest_framework import viewsets
from ..models import Tbforma
from ..serializers import FormaSerializer

class FormaViewSet(viewsets.ModelViewSet):
    queryset = Tbforma.objects.all()
    serializer_class = FormaSerializer