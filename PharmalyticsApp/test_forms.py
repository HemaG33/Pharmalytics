from django.test import TestCase
from .forms import CreateMedicationForm, CreateCustomerForm, MedicationOrderForm
from datetime import datetime
from .models import Medication

class MedicationFormTest(TestCase):
    def test_create_medication_form_valid(self):
        # Create valid form data
        form_data = {
            'name': 'Test Medication',
            'dosage': '10mg',
            'provider': 'Test Provider',
            'quantity': 100,
            'price': 50,
            'category': 'Blood Pressure',
            'description': 'Test Description',
            'sideeffects': 'Test Side Effects',
            'chemicalcomposition': 'Test Composition',
        }
        form = CreateMedicationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_medication_form_invalid(self):
        # Create invalid form data (missing required field)
        form_data = {
            'dosage': '10mg',
            'provider': 'Test Provider',
            'quantity': 100,
            'price': 50,
            'category': 'Blood Pressure',
            'description': 'Test Description',
            'sideeffects': 'Test Side Effects',
            'chemicalcomposition': 'Test Composition',
        }
        form = CreateMedicationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        
class CustomerFormTest(TestCase):
    def test_create_customer_form_valid(self):
        # Create valid form data
        form_data = {
            'name': 'Test Customer',
            'dateofbirth': datetime.now().strftime('%Y-%m-%d'),
            'gender': 'Male',
            'phonenumber': 1234567890,
            'insurancecompany': 'Test Insurance',
            'permanentmedication': 'Test Medication',
        }
        form = CreateCustomerForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_customer_form_invalid(self):
        # Create invalid form data (missing required field)
        form_data = {
            'dateofbirth': datetime.now().strftime('%Y-%m-%d'),
            'gender': 'Male',
            'phonenumber': 1234567890,
            'insurancecompany': 'Test Insurance',
            'permanentmedication': 'Test Medication',
        }
        form = CreateCustomerForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
class MedicationOrderFormTest(TestCase):
    def test_medication_order_form_valid(self):
        # Create valid form data
        form_data = {
            'provider': 'Test Provider',
            'provideremail': 'test@example.com',
            'medname': 'Test Medication',
            'dosage': '10mg',
            'quantity': 100,
            'notes': 'Test notes',
        }
        form = MedicationOrderForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_medication_order_form_invalid(self):
        # Create invalid form data (missing required field)
        form_data = {
            'provider': 'Test Provider',
            'provideremail': 'test@example.com',
            'dosage': '10mg',
            'quantity': 100,
            'notes': 'Test notes',
        }
        form = MedicationOrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('medname', form.errors)
        
class SalesTransactionFormTest(TestCase):
    def setUp(self):
        # Create a test medication for the form
        self.medication = Medication.objects.create(
            name='Test Medication',
            dosage='10mg',
            provider='Test Provider',
            quantity=100,
            expirydate='2022-12-31',
            price=50,
            category='Blood Pressure',
            description='Test Description',
            sideeffects='Test Side Effects',
            chemicalcomposition='Test Composition'
        )

    def test_sales_transaction_form_valid(self):
        # Create valid form data
        form_data = {
            'medication': self.medication.id,
            'quantity_sold': 10,
            'price_per_unit': 50,
            'payment_method': 'Credit Card',
            'customeremail': 'test@example.com',
        }
        form = SalesTransactionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_sales_transaction_form_invalid(self):
        # Create invalid form data (missing required field)
        form_data = {
            'quantity_sold': 10,
            'price_per_unit': 50,
            'payment_method': 'Credit Card',
            'customeremail': 'test@example.com',
        }
        form = SalesTransactionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('medication', form.errors)