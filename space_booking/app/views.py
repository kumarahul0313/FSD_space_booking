from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .models import Booking, MeetingRoom, Office, AdditionalServices
from .serializers import MeetingRoomSerializer, OfficeSerializer, AdditionalServicesSerializer
from django.http import HttpResponse
from rest_framework import status

# Create your views here.

class MeetingRoomViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    
    
class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    

class AdditionalServicesViewSet(viewsets.ModelViewSet):
    queryset = AdditionalServices.objects.all()
    serializer_class = AdditionalServicesSerializer
    

    


