from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .models import Booking, MeetingRoom
from .serializers import MeetingRoomSerializer, OfficeSerializer, AdditionalServicesSerializer


# Create your views here.

class MeetingRoomViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    
    
class OfficeViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all()
    serializer_class = OfficeSerializer
    

class AdditionalServicesViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all()
    serializer_class = AdditionalServicesSerializer
    

    


