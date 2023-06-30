from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Flight

# Form for user login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

# Form for user signup
class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')

# Form for flight search
class FlightSearchForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': 'HH:MM'}), required=False)

# Form for flight creation/update
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('flight_number', 'departure_city', 'destination_city', 'departure_time', 'arrival_time', 'seat_count')
