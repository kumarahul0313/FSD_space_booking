from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .models import Booking, MeetingRoom, Office, AdditionalServices
from .serializers import *
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, action, authentication_classes, permission_classes, throttle_classes
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


class BookingviewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for managing booking
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    http_method_names = ['get', 'post', 'put']
    
    def get_queryset(self):
        return self.queryset.filter(employee__pk=self.request.user.pk)
    
    @action(detail=True, methods=['get'])   
    def retrieve(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            if pk == str(self.request.user.pk):
                instance = self.queryset.filter(employee__pk=pk)
                serializer = self.get_serializer(instance, many=True)
                results = serializer.data
                msg = str(len(results)) + " booking details found."
                return Response({"results":results, "msg":msg, "code":200})
            else:
                msg = "You are not authorized to get the booking details."
                return Response({'code': '101', 'msg': msg})
        except Exception as e:
            return Response({"message" : "Exception in fetching booking","status":status.HTTP_400_BAD_REQUEST,"result":e})
        
    @action(detail=True, methods=['put'])   
    def update(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            booking_obj = self.queryset.filter(pk=pk)
            if booking_obj:
                serializer = BookingSerializer(data=request.data)
                if serializer.is_valid():
                    booking_obj.update(**serializer.data)
                    return Response({"message" : "Booking updated!!","status":status.HTTP_201_CREATED})
            return Response({"message" : "Error in updating booking details","status":status.HTTP_400_BAD_REQUEST,"result":"Booking not found!!"})
        except Exception as e:
            return Response({"message" : "Exception in adding booking","status":status.HTTP_400_BAD_REQUEST,"result":e})
     
    @action(detail=True, methods=['post'])   
    def create(self,request):
        try:
            serializers = BookingSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response({"message" : "Booking added!!","status":status.HTTP_201_CREATED})
            return Response({"message" : "Error in booking","status":status.HTTP_400_BAD_REQUEST,"result":serializers.errors})
        except Exception as e:
            return Response({"message" : "Exception in adding booking","status":status.HTTP_400_BAD_REQUEST,"result":e})
        
    @action(detail=True, methods=['post'])
    def cancel(self,request):
        try:
            pk = request.data.get('booking_id')
            booking_obj = self.queryset.filter(pk=pk)
            if booking_obj:
                booking_obj.delete()
                return Response({"message" : "Booking deleted!!","status":status.HTTP_201_CREATED})
            return Response({"message" : "Error in deleting booking details","status":status.HTTP_400_BAD_REQUEST,"result":"Booking not found!!"})
        except Exception as e:
            return Response({"message" : "Exception in deleting booking details","status":status.HTTP_400_BAD_REQUEST,"result":e})
            