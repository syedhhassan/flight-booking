from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm, FlightSearchForm
from .models import Flight, Booking
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    return render(request, 'base.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('flight_search')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def flight_search(request):
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            flights = Flight.objects.filter(departure_time__date=date)
            return render(request, 'flight_search_results.html', {'flights': flights})
    else:
        form = FlightSearchForm()
    return render(request, 'flight_search.html', {'form': form})

@login_required
def flight_search_results(request):
    form = FlightSearchForm(request.GET)
    if form.is_valid():
        date = form.cleaned_data['date']
        flights = Flight.objects.filter(departure_time_date=date)
        return render(request, 'flight_search_results.html', {'flight': flights})


@login_required
def book_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    if request.method == 'POST':
        seat_number = request.POST.get('seat_number')
        if not seat_number:
            return redirect('book_flight', flight_id=flight.id)
        seat_number = int(seat_number)
        if seat_number < 1 or seat_number > flight.seat_count:
            return redirect('book_flight', flight_id=flight.id)
        if Booking.objects.filter(flight=flight, seat_number=seat_number).exists():
            return redirect('book_flight', flight_id=flight.id)
        booking = Booking(user=request.user, flight=flight, seat_number=seat_number)
        booking.save()
        return redirect('my_bookings')
    return render(request, 'book_flight.html', {'flight': flight})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})


@login_required
@staff_member_required
def add_flight(request):
    if request.method == 'POST':
        # Process the flight creation form
        # Save the new flight object
        return redirect('flight_search')
    return render(request, 'add_flight.html')


@login_required
@staff_member_required
def remove_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    # Delete the flight object
    return redirect('flight_search')


@login_required
@staff_member_required
def view_bookings(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    bookings = Booking.objects.filter(flight=flight)
    return render(request, 'view_bookings.html', {'flight': flight, 'bookings': bookings})


def user_logout(request):
    logout(request)
    return redirect('login')
