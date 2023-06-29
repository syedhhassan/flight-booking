from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_flights, name='search_flights'),
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('add-flight/', views.add_flight, name='add_flight'),
    path('remove-flight/<int:flight_id>/', views.remove_flight, name='remove_flight'),
    path('view-bookings/<int:flight_id>/', views.view_bookings, name='view_bookings'),
]