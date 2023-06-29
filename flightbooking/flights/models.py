from django.db import models
from django.contrib.auth.models import User


class Flight(models.Model):
    number = models.CharField(max_length=10)
    departure_time = models.DateTimeField()
    seat_count = models.PositiveIntegerField(default=60)

    def __str__(self):
        return self.number

    def get_available_seats(self):
        bookings = self.bookings.count()
        return max(0, self.seat_count - bookings)

    def is_full(self):
        return self.get_available_seats() == 0


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='bookings')

    def __str__(self):
        return f"Booking #{self.id} - User: {self.user.username}, Flight: {self.flight.number}"