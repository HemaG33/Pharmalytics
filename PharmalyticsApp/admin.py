from django.contrib import admin
from .models import Medication, Customers, MedicationOrder

# Register your models here.

admin.site.register(Medication)
admin.site.register(Customers)
admin.site.register(MedicationOrder)
