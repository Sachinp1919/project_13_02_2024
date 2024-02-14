from rest_framework import viewsets
from .serializers import LaptopSerializer
from .models import Laptop


class LaptopViewSet(viewsets.ModelViewSet):
    serializer_class = LaptopSerializer
    queryset = Laptop.objects.all()