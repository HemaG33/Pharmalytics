from django.db import models


class Medication(models.Model):
    id =  models.AutoField(primary_key= True)
    name = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    expirydate = models.DateField()
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    chemicalcomposition = models.CharField(max_length=200)
 