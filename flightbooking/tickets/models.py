from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'auth_user'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='tickets_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='tickets_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    seat_count = models.IntegerField(default=60)

    def __str__(self):
        return self.flight_number


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    seat_number = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.flight.flight_number}"
