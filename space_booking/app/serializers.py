from rest_framework import serializers
from .models import Booking, MeetingRoom


class MeetingRoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeetingRoom
        fields = "__all__"
        