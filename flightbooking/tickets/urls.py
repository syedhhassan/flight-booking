from django.urls import path
from . import views

# URL patterns for the flight booking application
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('flight/search/', views.flight_search, name='flight_search'),
    path('flight/book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('my/bookings/', views.my_bookings, name='my_bookings'),
    path('admin/flight/add/', views.add_flight, name='add_flight'),
    path('admin/flight/remove/<int:flight_id>/', views.remove_flight, name='remove_flight'),
    path('admin/flight/bookings/<int:flight_id>/', views.view_bookings, name='view_bookings'),
    path('logout/', views.user_logout, name='logout'),
]
