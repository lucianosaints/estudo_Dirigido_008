from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Unidade, Sala, Status, Bem, Categoria
from .serializers import UnidadeSerializer, SalaSerializer, StatusSerializer, BemSerializer, CategoriaSerializer


class UnidadeViewSet(ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SalaViewSet(ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BemViewSet(ModelViewSet):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]