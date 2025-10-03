from rest_framework import viewsets
from .models import Bookings
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated

class BookingViewset(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer
