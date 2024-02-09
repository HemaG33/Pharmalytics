from .forms import CreateMedicationForm, CreateCustomerForm, MedicationSearchForm, CustomerSearchForm, MedicationOrderForm
from .models import Medication, Customers
from .util import get_substitutions
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'PharmalyticsApp/home.html')

########################### Medication Table ####################################################
def create_medication(request):
    if request.method == 'POST':
        form = CreateMedicationForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            name = formdata['name']
            dosage = formdata['dosage']
            provider = formdata['provider']
            quantity = formdata['quantity']
            expiry_date = formdata['expirydate']
            category = formdata['category']
            description = formdata['description']
            side_effects = formdata['sideeffects']
            chemical_composition = formdata['chemicalcomposition']

            Medication.objects.create(
                name=name,
                dosage=dosage,
                provider=provider,
                quantity=quantity,
                expirydate=expiry_date,
                category=category,
                description=description,
                sideeffects=side_effects,
                chemicalcomposition=chemical_composition
            )

            return HttpResponseRedirect('/PharmalyticsApp/success')
    else:
        form = CreateMedicationForm()

    return render(request, 'PharmalyticsApp/create_medication.html', {'form': form})

def medication_list(request):
    medications = Medication.objects.all()
    # Handling search 
    form = MedicationSearchForm(request.GET)
    if form.is_valid():
        search_term = form.cleaned_data.get('search')
        if search_term:
            medications = medications.filter(name__icontains=search_term)

    # Fetching distinct chemical compositions for filter dropdown
    chemical_compositions = Medication.objects.values_list('chemicalcomposition', flat=True).distinct()
    # Handling Filter
    chemical_composition_filter = request.GET.get('chemicalcomposition')
    if chemical_composition_filter:
        medications = medications.filter(chemicalcomposition=chemical_composition_filter)

    return render(request, 'PharmalyticsApp/medication_list.html', {'medications': medications, 'form': form, 'chemical_compositions': chemical_compositions})

def medication_detail(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    substitutions = get_substitutions(medication)
    return render(request, 'PharmalyticsApp/medication_detail.html', {'medication': medication, 'substitutions': substitutions})

def update_medication(request, pk):
    medication = get_object_or_404(Medication, pk=pk)

    if request.method == 'POST':
        form = CreateMedicationForm(request.POST)
        if form.is_valid():
            medication.name = form.cleaned_data['name']
            medication.dosage = form.cleaned_data['dosage']
            medication.provider = form.cleaned_data['provider']
            medication.quantity = form.cleaned_data['quantity']
            medication.expirydate = form.cleaned_data['expirydate']
            medication.category = form.cleaned_data['category']
            medication.description = form.cleaned_data['description']
            medication.barcode = form.cleaned_data['barcode']
            medication.sideeffects = form.cleaned_data['sideeffects']
            medication.chemicalcomposition = form.cleaned_data['chemicalcomposition']

            medication.save()

            return redirect('PharmalyticsApp:success')
    else:
        form = CreateMedicationForm(initial={
            'name': medication.name,
            'dosage': medication.dosage,
            'provider': medication.provider,
            'quantity': medication.quantity,
            'expirydate': medication.expirydate,
            'category': medication.category,
            'description': medication.description,
            'barcode': medication.barcode,
            'sideeffects': medication.sideeffects,
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


########################### Customers Table ####################################################
def create_customer(request):
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            name = formdata['name']
            date_of_birth = formdata['dateofbirth']
            gender = formdata['gender']
            phone_number = formdata['phonenumber']
            insurance_company = formdata['insurancecompany']
            permanent_medication = formdata['permanentmedication']

            Customers.objects.create(
                name=name,
                dateofbirth=date_of_birth,
                gender=gender,
                phonenumber=phone_number,
                insurancecompany=insurance_company,
                permanentmedication=permanent_medication
            )

            return HttpResponseRedirect('/PharmalyticsApp/success')
    else:
        form = CreateCustomerForm()

    return render(request, 'PharmalyticsApp/create_customer.html', {'form': form})

def customer_list(request):
    customers = Customers.objects.all()
    # Handling search 
    form = CustomerSearchForm(request.GET)
    if form.is_valid():
        search_term = form.cleaned_data.get('search')
        if search_term:
            customers = customers.filter(name__icontains=search_term)

    # Fetching distinct permanent medication for filter dropdown
    permanent_medications = Customers.objects.values_list('permanentmedication', flat=True).distinct()
    # Handling Filter
    permanent_medication_filter = request.GET.get('permanentmedication')
    if permanent_medication_filter:
        customers = customers.filter(permanentmedication=permanent_medication_filter)

    return render(request, 'PharmalyticsApp/customer_list.html', {'customers': customers, 'form': form, 'permanent_medications': permanent_medications})

def customer_detail(request, pk):
    customer = get_object_or_404(Customers, pk=pk)
    return render(request, 'PharmalyticsApp/customer_detail.html', {'customer': customer})

def update_customer(request, pk):
    customer = get_object_or_404(Customers, pk=pk)

    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            customer.name = form.cleaned_data['name']
            customer.dateofbirth = form.cleaned_data['dateofbirth']
            customer.gender = form.cleaned_data['gender']
            customer.phonenumber = form.cleaned_data['phonenumber']
            customer.insurancecompany = form.cleaned_data['insurancecompany']
            customer.permanentmedication = form.cleaned_data['permanentmedication']
            customer.save()

            return redirect('PharmalyticsApp:success')
    else:
        form = CreateCustomerForm(initial={
            'name': customer.name,
            'dateofbirth': customer.dateofbirth,
            'gender': customer.gender,
            'phonenumber': customer.phonenumber,
            'insurancecompany': customer.insurancecompany,
            'permanentmedication': customer.permanentmedication,
        })

    return render(request, 'PharmalyticsApp/update_customer.html', {'form': form})

# Delete operation
def delete_customer(request, pk):
    customer = get_object_or_404(Customers, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('PharmalyticsApp:home')
    return render(request, 'PharmalyticsApp/delete_customer.html', {'customer': customer})

def success(request):
    return render(request, 'PharmalyticsApp/success.html')

########################### Submit Order ####################################################
def submit_order(request):
    if request.method == 'POST':
        form = MedicationOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            send_order_email(order)
            return HttpResponseRedirect('/PharmalyticsApp/success')  
    else:
        form = MedicationOrderForm()
    return render(request, 'PharmalyticsApp/submit_order.html', {'form': form})

def send_order_email(order):
    subject = 'New Medication Order'
    message = f'''
    Dear {order.provider},
    We request a new order for:
    Medication: {order.medname}
    Dosage: {order.dosage}
    Quantity: {order.quantity}
    Notes: {order.notes}
    Thank you in advance.
    Best Regards.'''
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [order.provideremail]
    send_mail(subject, message, from_email, recipient_list)

########################### Scan Barcode ####################################################
def scan_barcode(request):
    if request.method == 'POST':
        scanned_barcode = request.POST.get('barcode', '')
        medication = get_object_or_404(Medication, barcode=scanned_barcode)
        return render(request, 'PharmalyticsApp/medication_detail.html', {'medication': medication})
    return render(request, 'PharmalyticsApp/scan_barcode.html')