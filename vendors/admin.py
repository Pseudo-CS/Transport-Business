# vendors/admin.py
from django.contrib import admin
from .models import TransportOrder, TransportProposal

admin.site.register(TransportOrder)
admin.site.register(TransportProposal)