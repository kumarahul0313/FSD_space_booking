from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Office(models.Model):
    office_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    floor_number = models.IntegerField()

class MeetingRoom(models.Model):
    meetingroom_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    is_reservable = models.BooleanField(default=True)
    capacity = models.IntegerField()
    office = models.ForeignKey(Office, on_delete=models.CASCADE)

class Employee(User):
    employee_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=100)
    banned = models.BooleanField(default=False)

class AdditionalServices(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    service_description = models.CharField(max_length=100)
    
    
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.PROTECT)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.IntegerField() # in minutes
    recurring = models.BooleanField(default=False)
    recurring_type = models.CharField(max_length=20, blank=True, null=True)
    additional_requests = models.ForeignKey(AdditionalServices, on_delete=models.PROTECT )
    approval_required = models.BooleanField(default=False)
    booking_status = models.CharField(max_length=20, default='approved')
    approval_status = models.CharField(max_length=20, default='pending')
    pending_with = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    approved_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    
    
    
class Notification_log(models.Model):
    pass



    
    
    