from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
# from .forms import BookingForm

@login_required
def employee_register(request):
    if request.method == 'POST':
        # Process employee registration form submission
        pass
    else:
        # Render employee registration form
        pass

@login_required
def employee_bookings(request):
    employee = request.user.employee
    bookings = Booking.objects.filter(employee=employee)
    return render(request, 'employee_bookings.html', {'bookings': bookings})

@login_required
def employee_booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.employee = request.user.employee
            booking.save()
            messages.success(request, 'Booking created successfully!')
            return redirect('employee_bookings')
    else:
        form = BookingForm()
    return render(request, 'employee_booking_create.html', {'form': form})

@login_required
def hr_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'hr_bookings.html', {'bookings': bookings})

@login_required
def hr_booking_approval(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        status = request.POST.get('status')
        booking = get_object_or_404(Booking, pk=booking_id)
        booking.approval_status = status
        booking.save()
        messages.success(request, 'Booking approval status updated successfully!')
        return redirect('hr_bookings')
    else:
        # Render HR booking approval form
        pass

@login_required
def admin_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'admin_bookings.html', {'bookings': bookings})

@login_required
def admin_booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking created successfully!')
            return redirect('admin_bookings')
    else:
        form = BookingForm()
    return render(request, 'admin_booking_create.html', {'form': form})

@login_required
def admin_booking_update(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully!')
            return redirect('admin_bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'admin_booking_update.html', {'form': form})

@login_required
def admin_booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    booking.delete()
    messages.success(request, 'Booking deleted successfully!')
    return redirect('admin_bookings')
