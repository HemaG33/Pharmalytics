from django.test import TestCase
from .models import Medication, Customers, SalesTransaction
from datetime import datetime

class MedicationModelTest(TestCase):
    def setUp(self):
        self.medication = Medication.objects.create(
            name="Test Medication",
            dosage="10mg",
            provider="Test Provider",
            quantity=100,
            expirydate=datetime.now(),
            price=50,
            category="Blood Pressure",
            description="Test Description",
            barcode="1234567890123",
            sideeffects="Test Side Effects",
            chemicalcomposition="Test Composition",
            substitute="Test Substitute"
        )

    def test_medication_str(self):
        self.assertEqual(str(self.medication), "Test Medication")

    def test_name_max_length(self):
        max_length = self.medication._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_provider_max_length(self):
        max_length = self.medication._meta.get_field('provider').max_length
        self.assertEquals(max_length, 100)

    def test_quantity_default(self):
        self.assertEquals(self.medication.quantity, 100)

    def test_expiry_date(self):
        self.assertIsInstance(self.medication.expirydate, datetime)
        
class CustomersModelTest(TestCase):
    def setUp(self):
        self.customer = Customers.objects.create(
            name="Test Customer",
            dateofbirth=datetime.now(),
            gender="Male",
            phonenumber=1234567890,
            insurancecompany="Test Insurance",
            permanentmedication="Test Medication"
        )

    def test_customer_str(self):
        self.assertEqual(str(self.customer), "Test Customer (ID: 1)")

    def test_name_max_length(self):
        max_length = self.customer._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_gender_choices(self):
        gender_choices = [choice[0] for choice in Customers.gender_choices.choices]
        self.assertIn(self.customer.gender, gender_choices)
        
class MedicationOrderModelTest(TestCase):
    def setUp(self):
        self.order = MedicationOrder.objects.create(
            provider="Test Provider",
            provideremail="test@example.com",
            medname="Test Medication",
            dosage="10mg",
            quantity=50,
            notes="Test Notes",
            orderdate=datetime.now()
        )

    def test_order_provider_max_length(self):
        max_length = self.order._meta.get_field('provider').max_length
        self.assertEquals(max_length, 100)

    def test_order_medname_max_length(self):
        max_length = self.order._meta.get_field('medname').max_length
        self.assertEquals(max_length, 100)

    def test_order_notes_blank(self):
        self.assertTrue(self.order._meta.get_field('notes').blank)
        
class SalesTransactionModelTest(TestCase):
    def setUp(self):
        self.medication = Medication.objects.create(
            name="Test Medication",
            dosage="10mg",
            provider="Test Provider",
            quantity=100,
            expirydate=datetime.now(),
            price=50,
            category="Blood Pressure",
            description="Test Description",
            barcode="1234567890123",
            sideeffects="Test Side Effects",
            chemicalcomposition="Test Composition",
            substitute="Test Substitute"
        )
        self.customer = Customers.objects.create(
            name="Test Customer",
            dateofbirth=datetime.now(),
            gender="Male",
            phonenumber=1234567890,
            insurancecompany="Test Insurance",
            permanentmedication="Test Medication"
        )
        self.sale = SalesTransaction.objects.create(
            medication=self.medication,
            quantity_sold=10,
            price_per_unit=50,
            payment_method="Cash",
            timestamp=datetime.now(),
            customer=self.customer,
            customeremail="test@example.com"
        )

    def test_sale_medication_quantity(self):
        self.assertEqual(self.sale.medication.quantity, 90)

    def test_sale_total_price(self):
        self.assertEqual(self.sale.total_price(), 500)
