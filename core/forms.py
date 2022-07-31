from django import forms
from .models import *


class Blood_Donor_Form(forms.ModelForm):
    class Meta:
        model = Blood_form
        fields = ['name', 'email', 'first_name', 'last_name', 'Age', 'blood_group', 'address', 'province', 'city', 'report', 'reason']

class User_extra_contact_form(forms.ModelForm):
    class Meta:
        model = User_extra_contact
        fields = ['phone_number', 'address', 'province', 'city', 'blood_group']