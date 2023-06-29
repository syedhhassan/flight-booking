from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Flight, Booking
from .forms import FlightForm


def search_flights(request):
    if request.method == 'POST':
        # Retrieve the search criteria from the form submission
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Perform the flight search based on the provided criteria
        flights = Flight.objects.filter(departure_time__date=date, departure_time__time=time)

        context = {
            'flights': flights,
        }
        return render(request, 'flights/search_flights.html', context)

    return render(request, 'flights/search_flights.html')


@login_required
def book_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)

    if flight.is_full():
        messages.error(request, 'Sorry, this flight is fully booked.')
        return redirect('search_flights')

    if request.method == 'POST':
        # Perform the flight booking logic
        booking = Booking(user=request.user, flight=flight)
        booking.save()
        messages.success(request, 'Flight booked successfully.')
        return redirect('my_bookings')

    context = {
        'flight': flight,
    }
    return render(request, 'flights/book_flight.html', context)


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)

    context = {
        'bookings': bookings,
    }
    return render(request, 'flights/my_bookings.html', context)


@login_required
def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flight added successfully.')
            return redirect('add_flight')
    else:
        form = FlightForm()

    context = {
        'form': form,
    }
    return render(request, 'flights/add_flight.html', context)


@login_required
def remove_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)

    if request.method == 'POST':
        flight.delete()
        messages.success(request, 'Flight removed successfully.')
        return redirect('remove_flight')

    context = {
        'flight': flight,
    }
    return render(request, 'flights/remove_flight.html', context)


@login_required
def view_bookings(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    bookings = Booking.objects.filter(flight=flight)

    context = {
        'flight': flight,
        'bookings': bookings,
    }
    return render(request, 'flights/view_bookings.html', context)