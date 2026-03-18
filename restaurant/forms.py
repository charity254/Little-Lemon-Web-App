from django.forms import ModelForm
from .models import Booking


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'date', 'time', 'guest_number', 'special_requests']
        widgets = {
            'date': __import__('django').forms.DateInput(attrs={'type':'date'}),
            'time':__import__('django').forms.TimeInput(attrs={'type':'time'}),
        }
