from rest_framework import serializers
from .models import Booking, MeetingRoom, Office, AdditionalServices


class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = "__all__"
        

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"
        
        
class AdditionalServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalServices
        fields = "__all__"
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"