# transport_management/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import *  # Import the index view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('vendors/', include('vendors.urls')),
    path('transporters/', include('transporters.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # For login/logout
    path('vendor/login/', vendor_login, name='vendor_login'),  # Vendor login
    path('transporter/login/', transporter_login, name='transporter_login'),  # Transporter login


]
