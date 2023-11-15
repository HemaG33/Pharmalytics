from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('PharmalyticsApp/', include('PharmalyticsApp.urls', namespace='PharmalyticsApp')),
    path('admin/', admin.site.urls),
]
