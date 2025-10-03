from rest_framework import serializers
from .models import Bookings

from Authenticate.models import User

from Trips.serializers import TripsSerializer

class UserrSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class BookingSerializer(serializers.ModelSerializer):
    # user = UserrSerializer(read_only=True)
    # trip_info = TripsSerializer(read_only=True)
    class Meta:
        model = Bookings
        fields = ['id', 'user', 'trip', 'seats_quantity', 'status']
        read_only_fields = ['status', 'user']

    # def validate(self, data):
    #     if data['seats'] > data['trip']


        
    
