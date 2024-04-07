from django.urls import path
from .views import create_medication, medication_list, medication_detail, update_medication, delete_medication, home, success, create_customer, delete_customer, customer_detail, customer_list, update_customer
from .views import submit_order, order_list, order_detail, delete_order, scan_barcode, reorder_order, create_sale, sale_list, sale_detail, delete_sale, sale_error, SalesQuantityDataView, PriceTimeDataView, CustomerMedicationDataView

app_name = 'PharmalyticsApp'

urlpatterns = [
    path('success/', success, name='success'),
    path('medication/', medication_list, name='medication_list'),
    path('medication/<int:pk>/', medication_detail, name='medication_detail'),
    path('medication/<int:pk>/update/', update_medication, name='update_medication'),
    path('medication/<int:pk>/delete/', delete_medication, name='delete_medication'),
    path('createmedication/', create_medication, name='create_medication'),
    path('customer/', customer_list, name='customer_list'),
    path('customer/<int:pk>/', customer_detail, name='customer_detail'),
    path('customer/<int:pk>/update/', update_customer, name='update_customer'),
    path('customer/<int:pk>/delete/', delete_customer, name='delete_customer'),
    path('createcustomer/', create_customer, name='create_customer'),
    path('submitorder/', submit_order, name='submit_order'),
    path('order/', order_list, name='order_list'),
    path('order/<int:pk>/', order_detail, name='order_detail'),
    path('reorderorder/<int:pk>/', reorder_order, name='reorder_order'),
    path('order/<int:pk>/delete/', delete_order, name='delete_order'),
    path('scanbarcode/', scan_barcode, name='scan_barcode'),
    path('create-sale/', create_sale, name='create_sale'),
    path('sales/', sale_list, name='sale_list'),
    path('sales/<int:pk>/', sale_detail, name='sale_detail'),
    path('sales/<int:pk>/delete/', delete_sale, name='delete_sale'),
    path('sale-error/', sale_error, name='sale_error'),
    path('sales-quantity-chart/', SalesQuantityDataView.as_view(), name='sales_quantity_chart'),
    path('price-time-chart/', PriceTimeDataView.as_view(), name='price_time_chart'),
    path('customer-medication-chart/', CustomerMedicationDataView.as_view(), name='customer_medication_chart'),
    path('', home, name='home')
]