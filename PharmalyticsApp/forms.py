from django import forms
from .models import Medication, Customers, MedicationOrder

class CreateMedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'dosage','provider', 'quantity', 'expirydate', 'price','category', 'description', 'sideeffects','chemicalcomposition']
        widgets = {
            'expirydate': forms.DateInput(attrs={'type': 'date'}),
        }

    name = forms.CharField(label='Name')
    dosage = forms.CharField(label='Dosage')
    provider = forms.CharField(label='Provider')
    quantity = forms.IntegerField(label='Quantity')
    #expirydate = forms.DateField(label='Expiry Date')
    price = forms.IntegerField(label='Price')
    category_choices = Medication.category_choices.choices
    category = forms.ChoiceField(label='Category', choices=category_choices)
    description = forms.CharField(label='Description')
    sideeffects = forms.CharField(label='Side Effects')
    chemicalcomposition = forms.CharField(label='Chemical Composition')
    
class MedicationFilterForm(forms.Form):
    search = forms.CharField(required=False)
    #category = forms.CharField(required=False)

class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'dateofbirth', 'gender', 'phonenumber', 'insurancecompany', 'permanentmedication']
        widgets = {
            'dateofbirth': forms.DateInput(attrs={'type': 'date'}),
        }

    name = forms.CharField(label='Full Name')
    #dateofbirth = forms.DateField(label='Date of Birth')
    gender_choices = Customers.gender_choices.choices
    gender = forms.ChoiceField(label='Gender', choices=gender_choices)
    phonenumber = forms.IntegerField(label='Phone Number')
    insurancecompany = forms.CharField(label='Insurance Company')
    permanentmedication = forms.CharField(label='Permanent Medication')

class CustomerFilterForm(forms.Form):
    search = forms.CharField(required=False)
    #type = forms.CharField(required=False)

# Order Form
class MedicationOrderForm(forms.ModelForm):
    class Meta:
        model = MedicationOrder
        fields = ['provider', 'provideremail', 'medname', 'dosage', 'quantity', 'notes']
    