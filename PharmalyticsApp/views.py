from .forms import CreateMedicationForm, CreateCustomerForm, MedicationFilterForm, CustomerFilterForm
from .models import Medication, Customers
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def home(request):
    return render(request, 'PharmalyticsApp/home.html')

########################### Medication Table ####################################################
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
    # Handling search and filter
    form = MedicationFilterForm(request.GET)
    if form.is_valid():
        search_term = form.cleaned_data.get('search')
        #category_filter = form.cleaned_data.get('category')

        if search_term:
            medications = medications.filter(name__icontains=search_term)

        #if category_filter:
            #medications = medications.filter(category__icontains=category_filter)
    return render(request, 'PharmalyticsApp/medication_list.html', {'medications': medications, 'form': form})

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
    # Handling search and filter
    form = CustomerFilterForm(request.GET)
    if form.is_valid():
        search_term = form.cleaned_data.get('search')
        #type_filter = form.cleaned_data.get('type')

        if search_term:
            customers = customers.filter(name__icontains=search_term)

        #if type_filter:
            #customers = customers.filter(type=type_filter)
    return render(request, 'PharmalyticsApp/customer_list.html', {'customers': customers, 'form': form})

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
