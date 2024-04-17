from django.conf.urls import url
from django.urls import include
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'meeting_rooms', views.MeetingRoomViewSet, 'meeting_rooms')
router.register(r'offices', views.OfficeViewSet, 'offices')
router.register(r'addt_services', views.AdditionalServicesViewSet, 'addt_services')


urlpatterns = [
    url(r'^space_booking/', include(router.urls)),   
    
    
]
