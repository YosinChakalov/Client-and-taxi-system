from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class TripsAPIView(viewsets.ModelViewSet):
    queryset = Trips.objects.filter(available='available')
    serializer_class = TripsSerializer
    permission_classes = [IsAuthenticated,TripPermission]

    filter_backends = [DjangoFilterBackend,SearchFilter]
    
    filterset_fields = [ 'time','price' ]

    search_fields = ['title', 'from_where', 'to_where', ]

    def perform_create(self, serializer):
        serializer.save(driver_id=self.request.user)

    