# forms.py
from django import forms

class OrderForm(forms.Form):
    address = forms.CharField(max_length=100)
    quantity = forms.IntegerField()
    phone_number = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    zipcode = forms.IntegerField()
