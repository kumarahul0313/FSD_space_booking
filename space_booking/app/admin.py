from django.contrib import admin
from .models import MeetingRoom, Office, Employee, AdditionalServices, Booking

# Register your models here.

admin.site.register(MeetingRoom)
admin.site.register(Office)
admin.site.register(Employee)
admin.site.register(AdditionalServices)
admin.site.register(Booking)
