from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Medication, Customers, MedicationOrder, SalesTransaction
from .views import *

class MedicationViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_create_medication_view(self):
        url = reverse('PharmalyticsApp:create_medication')
        request = self.factory.get(url)
        response = create_medication(request)
        self.assertEqual(response.status_code, 200)

    def test_medication_list_view(self):
        # Create sample medication records
        medication1 = Medication.objects.create(name="Medication 1", dosage="5mg", provider="Provider A", quantity=100, expirydate="2024-04-30", price=10, category="Blood Pressure", description="Description 1", barcode="1234567890123", sideeffects="Side effects 1", chemicalcomposition="Composition 1", substitute="Substitute 1")
        medication2 = Medication.objects.create(name="Medication 2", dosage="10mg", provider="Provider B", quantity=50, expirydate="2024-05-15", price=20, category="Diabetes", description="Description 2", barcode="9876543210987", sideeffects="Side effects 2", chemicalcomposition="Composition 2", substitute="Substitute 2")

        url = reverse('PharmalyticsApp:medication_list')
        request = self.factory.get(url)
        response = medication_list(request)
        self.assertEqual(response.status_code, 200)

        # Test if the response contains medications
        self.assertQuerysetEqual(
            response.context['medications'],
            Medication.objects.all(),
            transform=lambda x: x
        )

    def test_medication_detail_view(self):
        # Create a sample medication
        medication = Medication.objects.create(name="Test Medication", dosage="10mg", provider="Test Provider", quantity=50, expirydate="2024-06-30", price=15, category="Other", description="Test Description", barcode="1234567890123", sideeffects="Test Side Effects", chemicalcomposition="Test Composition", substitute="Test Substitute")

        url = reverse('PharmalyticsApp:medication_detail', kwargs={'pk': medication.pk})
        request = self.factory.get(url)
        response = medication_detail(request, pk=medication.pk)
        self.assertEqual(response.status_code, 200)

        # Test if the response contains the correct medication
        self.assertEqual(response.context['medication'], medication)

    def test_update_medication_view(self):
        # Create a sample medication
        medication = Medication.objects.create(name="Test Medication", dosage="10mg", provider="Test Provider", quantity=50, expirydate="2024-06-30", price=15, category="Other", description="Test Description", barcode="1234567890123", sideeffects="Test Side Effects", chemicalcomposition="Test Composition", substitute="Test Substitute")

        url = reverse('PharmalyticsApp:update_medication', kwargs={'pk': medication.pk})
        request = self.factory.get(url)
        response = update_medication(request, pk=medication.pk)
        self.assertEqual(response.status_code, 200)

        # Test if the response contains the medication form
        self.assertTrue('form' in response.context)

    def test_delete_medication_view(self):
        # Create a sample medication
        medication = Medication.objects.create(name="Test Medication", dosage="10mg", provider="Test Provider", quantity=50, expirydate="2024-06-30", price=15, category="Other", description="Test Description", barcode="1234567890123", sideeffects="Test Side Effects", chemicalcomposition="Test Composition", substitute="Test Substitute")

        url = reverse('PharmalyticsApp:delete_medication', kwargs={'pk': medication.pk})
        request = self.factory.post(url)
        response = delete_medication(request, pk=medication.pk)
        self.assertEqual(response.status_code, 302)  # Redirects after deletion

        # Check if the medication has been deleted
        self.assertFalse(Medication.objects.filter(pk=medication.pk).exists())
        
class CustomerViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_create_customer_view(self):
        url = reverse('PharmalyticsApp:create_customer')
        request = self.factory.get(url)
        response = create_customer(request)
        self.assertEqual(response.status_code, 200)

    def test_customer_list_view(self):
        # Create sample customer records
        customer1 = Customers.objects.create(name="Customer 1", dateofbirth="1990-01-01", gender="Male", phonenumber=1234567890, insurancecompany="Insurance A", permanentmedication="Medication A")
        customer2 = Customers.objects.create(name="Customer 2", dateofbirth="1985-05-15", gender="Female", phonenumber=9876543210, insurancecompany="Insurance B", permanentmedication="Medication B")

        url = reverse('PharmalyticsApp:customer_list')
        request = self.factory.get(url)
        response = customer_list(request)
        self.assertEqual(response.status_code, 200)

        # Test if the response contains customers
        self.assertQuerysetEqual(
            response.context['customers'],
            Customers.objects.all(),
            transform=lambda x: x
        )

    def test_customer_detail_view(self):
        # Create a sample customer
        customer = Customers.objects.create(name="Test Customer", dateofbirth="1980-07-15", gender="Other", phonenumber=5555555555, insurancecompany="Test Insurance", permanentmedication="Test Medication")

        url = reverse('PharmalyticsApp:customer_detail', kwargs={'pk': customer.pk})
        request = self.factory.get(url)
        response = customer_detail(request, pk=customer.pk)
        self.assertEqual(response.status_code, 200)

        # Test if the response contains the correct customer
        self.assertEqual(response.context['customer'], customer)

    def test_update_customer_view(self):
        # Create a sample customer
        customer = Customers.objects.create(name="Test Customer", dateofbirth="1980-07-15", gender="Other", phonenumber=5555555555, insurancecompany="Test Insurance", permanentmedication="Test Medication")

        url = reverse('PharmalyticsApp:update_customer', kwargs={'pk': customer.pk})
        request = self.factory.get(url)
        response = update_customer(request, pk=customer.pk)
        self.assertEqual(response.status_code, 200)

        # Test if the response contains the customer form
        self.assertTrue('form' in response.context)

    def test_delete_customer_view(self):
        # Create a sample customer
        customer = Customers.objects.create(name="Test Customer", dateofbirth="1980-07-15", gender="Other", phonenumber=5555555555, insurancecompany="Test Insurance", permanentmedication="Test Medication")

        url = reverse('PharmalyticsApp:delete_customer', kwargs={'pk': customer.pk})
        request = self.factory.post(url)
        response = delete_customer(request, pk=customer.pk)
        self.assertEqual(response.status_code, 302)  # Redirects after deletion

        # Check if the customer has been deleted
        self.assertFalse(Customers.objects.filter(pk=customer.pk).exists())
class MedicationOrderViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_submit_order_view(self):
        url = reverse('PharmalyticsApp:submit_order')
        request = self.factory.get(url)
        response = submit_order(request)
        self.assertEqual(response.status_code, 200)

    def test_order_list_view(self):
        # Create sample medication order records
        order1 = MedicationOrder.objects.create(provider="Provider A", provideremail="providerA@example.com", medname="Medication A", dosage="10mg", quantity=20, notes="Test note 1")
        order2 = MedicationOrder.objects.create(provider="Provider B", provideremail="providerB@example.com", medname="Medication B", dosage="20mg", quantity=30, notes="Test note 2")

        url = reverse('PharmalyticsApp:order_list')
        request = self.factory.get(url)
        response = order_list(request)
        self.assertEqual(response.status_code, 200)

        # Test if the response contains medication orders
        self.assertQuerysetEqual(
            response.context['orders'],
            MedicationOrder.objects.all(),
            transform=lambda x: x
        )

    def test_order_detail_view(self):
        # Create a sample medication order
        order = MedicationOrder.objects.create(provider="Provider X", provideremail="providerX@example.com", medname="Medication X", dosage="15mg", quantity=25, notes="Test note")

        url = reverse('PharmalyticsApp:order_detail', kwargs={'pk': order.pk})
        request = self.factory.get(url)
        response = order_detail(request, pk=order.pk)
        self.assertEqual(response.status_code, 200)

        # Test if the response contains the correct order
        self.assertEqual(response.context['order'], order)

    def test_reorder_order_view(self):
        # Create a sample medication order
        order = MedicationOrder.objects.create(provider="Provider Y", provideremail="providerY@example.com", medname="Medication Y", dosage="5mg", quantity=10, notes="Test note")

        url = reverse('PharmalyticsApp:reorder_order', kwargs={'pk': order.pk})
        request = self.factory.get(url)
        response = reorder_order(request, pk=order.pk)
        self.assertEqual(response.status_code, 200)

        # Test if the response contains the order form
        self.assertTrue('form' in response.context)

    def test_delete_order_view(self):
        # Create a sample medication order
        order = MedicationOrder.objects.create(provider="Provider Z", provideremail="providerZ@example.com", medname="Medication Z", dosage="25mg", quantity=15, notes="Test note")

        url = reverse('PharmalyticsApp:delete_order', kwargs={'pk': order.pk})
        request = self.factory.post(url)
        response = delete_order(request, pk=order.pk)
        self.assertEqual(response.status_code, 302)  # Redirects after deletion

        # Check if the order has been deleted
        self.assertFalse(MedicationOrder.objects.filter(pk=order.pk).exists())
        
class SalesTransactionViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        # Create sample medication and customer records
        self.medication = Medication.objects.create(name="Medication X", dosage="10mg", provider="Provider X", quantity=50, expirydate="2024-12-31", price=100, category="PAIN", description="Test medication", barcode="1234567890123", sideeffects="None", chemicalcomposition="Test composition", substitute="None")
        self.customer = Customers.objects.create(name="Customer Y", dateofbirth="1990-01-01", gender="Male", phonenumber=1234567890, insurancecompany="Company Y", permanentmedication="Medication Y")

    def test_create_sale_view(self):
        url = reverse('PharmalyticsApp:create_sale')
        request = self.factory.get(url)
        response = create_sale(request)
        self.assertEqual(response.status_code, 200)

    def test_sale_list_view(self):
        # Create sample sales transaction records
        sale1 = SalesTransaction.objects.create(medication=self.medication, quantity_sold=10, price_per_unit=100, payment_method="Cash", customer=self.customer, customeremail="customerY@example.com")
        sale2 = SalesTransaction.objects.create(medication=self.medication, quantity_sold=20, price_per_unit=200, payment_method="Card", customer=self.customer, customeremail="customerY@example.com")

        url = reverse('PharmalyticsApp:sale_list')
        request = self.factory.get(url)
        response = sale_list(request)
        self.assertEqual(response.status_code, 200)

        # Test if the response contains sales transactions
        self.assertQuerysetEqual(
            response.context['sales'],
            SalesTransaction.objects.all(),
            transform=lambda x: x
        )

    def test_sale_detail_view(self):
        # Create a sample sales transaction
        sale = SalesTransaction.objects.create(medication=self.medication, quantity_sold=15, price_per_unit=150, payment_method="Online", customer=self.customer, customeremail="customerY@example.com")

        url = reverse('PharmalyticsApp:sale_detail', kwargs={'pk': sale.pk})
        request = self.factory.get(url)
        response = sale_detail(request, pk=sale.pk)
        self.assertEqual(response.status_code, 200)

        # Test if the response contains the correct sale
        self.assertEqual(response.context['sale'], sale)

    def test_delete_sale_view(self):
        # Create a sample sales transaction
        sale = SalesTransaction.objects.create(medication=self.medication, quantity_sold=25, price_per_unit=250, payment_method="Cash", customer=self.customer, customeremail="customerY@example.com")

        url = reverse('PharmalyticsApp:delete_sale', kwargs={'pk': sale.pk})
        request = self.factory.post(url)
        response = delete_sale(request, pk=sale.pk)
        self.assertEqual(response.status_code, 302)  # Redirects after deletion

        # Check if the sale has been deleted
        self.assertFalse(SalesTransaction.objects.filter(pk=sale.pk).exists())