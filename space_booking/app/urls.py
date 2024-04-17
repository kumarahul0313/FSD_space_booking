from django.conf.urls import url
from django.urls import include
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'meeting_rooms', views.MeetingRoomViewSet)
router.register(r'offices', views.OfficeViewSet)
router.register(r'addt_services', views.AdditionalServicesViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    
    
    
    path("", )
    
    
    
]
