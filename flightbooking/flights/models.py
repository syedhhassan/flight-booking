from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    seats = models.IntegerField(default=60)

    def __str__(self):
        return f"Flight {self.flight_number} - {self.date} {self.time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} - {self.user.username} ({self.flight.flight_number})"