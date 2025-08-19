from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, MateriaSerializer, Nota_AlunoSerializer
from django.contrib.auth import get_user_model
from .models import User, Materia, Nota_Aluno


class UserView(generics.CreateAPIView):
    """
    Endpoint para cadastro de usuários “normais”.
    Usa o UserSerializer.create() para fazer o hashing da senha.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Implemente sua lógica GET aqui
        # Exemplo: listar usuários
        User = get_user_model()
        users = User.objects.all()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

class MateriaView(generics.ListCreateAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class NotaView(generics.ListCreateAPIView):
    queryset = Nota_Aluno.objects.all()
    serializer_class = Nota_AlunoSerializer
