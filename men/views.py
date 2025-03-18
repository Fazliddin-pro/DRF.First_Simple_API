from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from django.shortcuts import render

from men.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from .models import Category, Men
from .serializers import MenSerializer


# class MenViewSet(viewsets.ModelViewSet):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get("pk")

#         if not pk:
#             return Men.objects.all()[:3]

#         return Men.objects.filter(pk=pk)

#     @action(methods=['GET'], detail=False)
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})


class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = [IsOwnerOrReadOnly]


class MenAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = [IsAdminOrReadOnly]
