from rest_framework import viewsets
from .models import Bookings
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserOrAdmin, IsOwnerOrAdmin

class BookingViewset(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsUserOrAdmin, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
