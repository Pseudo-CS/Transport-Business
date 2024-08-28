# vendors/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', vendor_dashboard, name='vendor_dashboard'),  # Vendor dashboard
    path('create_order/', create_order, name='create_order'),
    path('orders/<int:order_id>/proposals/', view_proposals, name='view_proposals'),
    path('proposals/<int:proposal_id>/accept/', accept_proposal, name='accept_proposal'),
]
