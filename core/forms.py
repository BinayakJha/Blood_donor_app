from django import forms
from .models import *


class Blood_Donor_Form(forms.ModelForm):
    class Meta:
        model = Blood_form
        fields = ['name', 'email', 'first_name', 'last_name', 'Age', 'blood_group', 'address', 'province', 'city', 'report', 'reason']