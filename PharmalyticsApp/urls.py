from django.urls import path
from .views import create_medication, medication_list, medication_detail, update_medication, delete_medication, home, success

app_name = 'PharmalyticsApp'

urlpatterns = [
    path('success/', success, name='success'),
    path('medication/', medication_list, name='medication_list'),
    path('medication/<int:pk>/', medication_detail, name='medication_detail'),
    path('medication/<int:pk>/update/', update_medication, name='update_medication'),
    path('medication/<int:pk>/delete/', delete_medication, name='delete_medication'),
    path('create/', create_medication, name='create_medication'),
    path('', home, name='home')
]