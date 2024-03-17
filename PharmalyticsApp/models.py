from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError


# Medication Model
class Medication(models.Model):
    class category_choices(models.TextChoices):
        BLOOD = 'Blood Pressure',
        DIABETES ='Diabetes',
        GASTRO ='Gastro',
        PREGNANCY ='Pregnancy',
        INFANTS ='Infants',
        PAIN = 'Pain Killer',
        OTHER = 'Other'
    

    id =  models.AutoField(primary_key= True)
    name = models.CharField(max_length=50)
    dosage = models.CharField(max_length=10, null=True)
    provider = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    expirydate = models.DateField()
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50, choices=category_choices.choices, default=category_choices.BLOOD)
    description = models.CharField(max_length=200)
    barcode = models.CharField(max_length=13, unique=True, null=True)
    sideeffects = models.CharField(max_length=200, null=True)
    chemicalcomposition = models.CharField(max_length=200, null=True)
    substitute = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name
 
# Customers Model
class Customers(models.Model):
    class gender_choices(models.TextChoices): 
        FEMALE = 'Female',
        MALE = 'Male',
        OTHER = 'Other',
        NOSPECIFY = 'Prefer not to specify'
    

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=25, choices=gender_choices.choices, null=True)
    phonenumber = models.IntegerField()
    insurancecompany = models.CharField(max_length=50, null=True)
    permanentmedication = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return f"{self.name} (ID: {self.id})"
    
# Order Model
class MedicationOrder(models.Model):
    id = models.AutoField(primary_key=True)
    provider = models.CharField(max_length=100)
    provideremail = models.EmailField()
    medname = models.CharField(max_length=100)
    dosage = models.CharField(max_length=20)
    quantity = models.IntegerField()
    notes = models.TextField(blank=True)
    orderdate = models.DateTimeField(default=datetime.now)
    
# Sales Model
class SalesTransaction(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    price_per_unit = models.IntegerField()
    payment_method = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=datetime.now)
    customer = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True, blank=True)

    def total_price(self):
        return self.quantity_sold * self.price_per_unit