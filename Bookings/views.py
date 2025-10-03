from rest_framework import viewsets
from .models import Bookings
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserOrAdmin, IsOwnerOrAdmin
from .pagination import BookingPagination

class BookingViewset(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer
    pagination_class = BookingPagination
    permission_classes = [IsAuthenticated, IsUserOrAdmin, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
