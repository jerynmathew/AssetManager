from rest_framework import viewsets

from .serializers import AssetSerializer
from .models import Assets


class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetSerializer

