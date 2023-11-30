from .models import Medication
from django.db.models import Q

def get_substitutions(medication):
    similar_medications = Medication.objects.filter(
        Q(chemicalcomposition__icontains=medication.chemicalcomposition) & ~Q(id=medication.id))[:5]
    return similar_medications
