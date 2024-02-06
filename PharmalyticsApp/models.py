from django.db import models

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
 
# Customers Model
class Customers(models.Model):
    class gender_choices(models.TextChoices): 
        FEMALE = 'Female',
        MALE = 'Male'
    

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_choices.choices, null=True)
    phonenumber = models.IntegerField()
    insurancecompany = models.CharField(max_length=50, null=True)
    permanentmedication = models.CharField(max_length=200, null=True)
    
# Order Model
class MedicationOrder(models.Model):
    id = models.AutoField(primary_key=True)
    provider = models.CharField(max_length=100)
    provideremail = models.EmailField()
    medname = models.CharField(max_length=100)
    dosage = models.CharField(max_length=20)
    quantity = models.IntegerField()
    notes = models.TextField(blank=True)
