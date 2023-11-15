from django import forms
from .models import Medication

class CreateMedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'provider', 'quantity', 'expirydate', 'category', 'description', 'chemicalcomposition']
        
    # If you want to customize labels or widgets, you can do so here
    name = forms.CharField(label='Name')
    provider = forms.CharField(label='Provider')
    quantity = forms.IntegerField(label='Quantity')
    expirydate = forms.DateField(label='Expiry Date')
    category = forms.CharField(label='Category')
    description = forms.CharField(label='Description')
    chemicalcomposition = forms.CharField(label='Chemical Composition')
