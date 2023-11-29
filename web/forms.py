from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ["timestamp"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'box', 'placeholder': 'enter your name', 'required': True, 'maxlength': 50}),
            'email': forms.EmailInput(attrs={'class': 'box', 'placeholder': 'enter your email', 'required': True, 'maxlength': 50}),
            'number': forms.NumberInput(attrs={'class': 'box', 'placeholder': 'enter your number', 'required': True, 'maxlength': 50}),
            'message': forms.Textarea(attrs={'class': 'box', 'placeholder': 'enter your message', 'required': True, 'maxlength': 1000, 'cols': 30, 'rows': 10}),
        }
