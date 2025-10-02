from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class TripsAPIView(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(driver_id=self.request.user)

    