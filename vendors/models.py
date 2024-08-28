# vendors/models.py
from django.contrib.auth.models import User
from django.db import models

class TransportOrder(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    transporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='accepted_orders', blank=True)
    quoted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('DECLINED', 'Declined')], default='PENDING')

    def __str__(self):
        return f"{self.product} - {self.vendor.username}"


class TransportProposal(models.Model):
    order = models.ForeignKey(TransportOrder, on_delete=models.CASCADE, related_name='proposals')
    transporter = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')  # Can be 'Pending', 'Accepted', etc.