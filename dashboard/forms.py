from socket import fromshare
from django import forms
from .models import product,order

class product_form(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'

class order_form(forms.ModelForm):
    class Meta:
        model=order
        fields=['product','order_quantity']
