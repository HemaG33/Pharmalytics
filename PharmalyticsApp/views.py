from .forms import CreateMedicationForm
from .models import Medication
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def home(request):
    return render(request, 'PharmalyticsApp/home.html')

def create_medication(request):
    if request.method == 'POST':
        form = CreateMedicationForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            name = formdata['name']
            provider = formdata['provider']
            quantity = formdata['quantity']
            expiry_date = formdata['expirydate']
            category = formdata['category']
            description = formdata['description']
            chemical_composition = formdata['chemicalcomposition']

            Medication.objects.create(
                name=name,
                provider=provider,
                quantity=quantity,
                expirydate=expiry_date,
                category=category,
                description=description,
                chemicalcomposition=chemical_composition
            )

            return HttpResponseRedirect('/PharmalyticsApp/success')
    else:
        form = CreateMedicationForm()

    return render(request, 'PharmalyticsApp/create_medication.html', {'form': form})

def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'PharmalyticsApp/medication_list.html', {'medications': medications})

def medication_detail(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    return render(request, 'PharmalyticsApp/medication_detail.html', {'medication': medication})

def update_medication(request, pk):
    medication = get_object_or_404(Medication, pk=pk)

    if request.method == 'POST':
        form = CreateMedicationForm(request.POST)
        if form.is_valid():
            medication.name = form.cleaned_data['name']
            medication.provider = form.cleaned_data['provider']
            medication.quantity = form.cleaned_data['quantity']
            medication.expirydate = form.cleaned_data['expirydate']
            medication.category = form.cleaned_data['category']
            medication.description = form.cleaned_data['description']
            medication.chemicalcomposition = form.cleaned_data['chemicalcomposition']

            medication.save()

            return redirect('PharmalyticsApp:success')
    else:
        form = CreateMedicationForm(initial={
            'name': medication.name,
            'provider': medication.provider,
            'quantity': medication.quantity,
            'expirydate': medication.expirydate,
            'category': medication.category,
            'description': medication.description,
            'chemicalcomposition': medication.chemicalcomposition,
        })

    return render(request, 'PharmalyticsApp/update_medication.html', {'form': form})

# Delete operation
def delete_medication(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    if request.method == 'POST':
        medication.delete()
        return redirect('PharmalyticsApp:home')
    return render(request, 'PharmalyticsApp/delete_medication.html', {'medication': medication})

def success(request):
    return render(request, 'PharmalyticsApp/success.html')


