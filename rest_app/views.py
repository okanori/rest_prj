from rest_framework import viewsets, filters

import django_filters

from .models import Position
from .serializer import PositionSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
