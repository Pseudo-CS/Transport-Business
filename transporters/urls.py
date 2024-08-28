# transporters/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', transporter_dashboard, name='transporter_dashboard'),
    path('view_order/<int:order_id>/', view_order, name='view_order'),
    path('accept_order/<int:order_id>/', accept_order, name='accept_order'),
    #path('decline_order/<int:order_id>/', decline_order, name='decline_order'),
]
