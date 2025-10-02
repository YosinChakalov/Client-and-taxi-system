from rest_framework import serializers
from .models import *

class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = ['id','title','from_where','to_where','price','seats','time','date','driver_id']
        read_only_fields = ['driver_id']