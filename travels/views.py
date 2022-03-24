from django.shortcuts import render
from rest_framework import generics
from .serializer import TravelSerializer
from .models import Travel
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class TravelList(generics.ListCreateAPIView):
  permission_classes=(IsAuthenticated,)
  queryset = Travel.objects.all()
  serializer_class = TravelSerializer

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes=(IsOwnerOrReadOnly,)
  permission_classes=(IsAuthenticated,)
  queryset = Travel.objects.all()
  serializer_class = TravelSerializer