# vendors/views.py
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.urls import reverse

from .models import TransportOrder, TransportProposal
from django.contrib.auth.decorators import login_required


@login_required
def vendor_dashboard(request):
    # Get all orders created by the logged-in vendor
    orders = TransportOrder.objects.filter(vendor=request.user)
    return render(request, 'vendor_dashboard.html', {'orders': orders})


@login_required
def view_proposals(request, order_id):
    # Get the order and its proposals
    order = get_object_or_404(TransportOrder, id=order_id, vendor=request.user)
    proposals = order.proposals.all() 
    return render(request, 'view_proposals.html', {'order': order, 'proposals': proposals})

@login_required  # Ensure that only logged-in users can create orders
def create_order(request):
    if request.method == 'POST':
        product = request.POST['product']
        quantity = request.POST['quantity']
        pickup = request.POST['pickup']
        destination = request.POST['destination']
        
        # Create and save the new order with the logged-in user as the vendor
        order = TransportOrder(
            product=product, 
            quantity=quantity, 
            pickup_location=pickup, 
            destination=destination, 
            vendor=request.user  # Set the vendor as the logged-in user
        )
        order.save()
        
        # Get all transporters' emails
        transporters = User.objects.filter(groups__name='Transporters') 
        transporter_emails = [transporter.email for transporter in transporters]
        
        # Generate the link to the view order page
        order_url = request.build_absolute_uri(reverse('view_order', args=[order.id]))

        # Send email to all transporters
        subject = 'New Transport Order Available'
        message = f'A new transport order has been created.\n\nProduct: {order.product}\nQuantity: {order.quantity}\nPickup: {order.pickup_location}\nDestination: {order.destination}\n\nClick here to view the order: {order_url}'
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            transporter_emails,
            fail_silently=False,
        )
        # Redirect to the vendor dashboard after successful order creation
        return redirect('vendor_dashboard')

    return render(request, 'create_order.html')


@login_required
def accept_proposal(request, proposal_id):
    # Get the proposal
    proposal = get_object_or_404(TransportProposal, id=proposal_id)
    
    # Update the status of the associated order and proposal
    proposal.order.status = 'ACCEPTED'
    proposal.status = 'Accepted'
    proposal.order.save()
    proposal.save()
    
    return redirect('vendor_dashboard')
