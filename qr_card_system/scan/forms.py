from django import forms
from .models import CardOwner

class CardOwnerForm(forms.ModelForm):
    class Meta:
        model = CardOwner
        fields = ['name', 'email', 'phone', 'hostel_name', 'room_number', 'card_uid']
        widgets = {
            'card_uid': forms.TextInput(attrs={'placeholder': 'Unique Card ID'}),
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'hostel_name': forms.TextInput(attrs={'placeholder': 'Hostel Name'}),
            'room_number': forms.TextInput(attrs={'placeholder': 'Room Number'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Contact Info'}),
        }