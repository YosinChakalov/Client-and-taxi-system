from rest_framework import serializers
from .models import Bookings

from Authenticate.models import User

from Trips.serializers import TripsSerializer


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookings
        fields = ['id', 'user', 'trip', 'seats_quantity', 'status']
        read_only_fields = ['status', 'user']

    def validate(self, data):
        trip = data['trip']
        seats = data['seats_quantity']
        if seats > trip.seats:
            raise serializers.ValidationError('Недостаточно мест в поездке')
        return data


        
    
