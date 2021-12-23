from django import forms
from .models import Appoinment

class AppoinmentForm(forms.ModelForm):
    class Meta:
        model = Appoinment
        fields = '__all__'

        widgets = {
            'f_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'l_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'subject':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject'}),
            'appointment_date':forms.DateInput(attrs={'class':'form-control', 'placeholder':'Appointment Date', 'type':'date'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone', 'type':'tel'}),
            'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'})
        }

