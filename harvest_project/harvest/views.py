from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Harvest
from .serializers import UserSerializer, HarvestSerializer
from rest_framework.exceptions import NotFound


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({
                'message': 'Usuário registrado com sucesso!',
                'user': UserSerializer(user).data,
                'access_token': access_token
            }, status=201)
        return Response(serializer.errors, status=400)


class HarvestListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HarvestSerializer

    def get_queryset(self):
        return Harvest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HarvestRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HarvestSerializer

    def get_queryset(self):
        return Harvest.objects.filter(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise NotFound(detail="Colheita não encontrada.")
        return obj
