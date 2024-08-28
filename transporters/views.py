# transporters/views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from vendors.models import TransportOrder, TransportProposal
from django.contrib.auth.decorators import login_required


@login_required
def transporter_dashboard(request):
    # Get all available orders that the transporter has not already submitted a proposal for
    available_orders = TransportOrder.objects.exclude(proposals__transporter=request.user)
    
    # Get all proposals that the transporter has submitted
    my_proposals = TransportProposal.objects.filter(transporter=request.user)
    
    return render(request, 'transporter_dashboard.html', {
        'available_orders': available_orders,
        'my_proposals': my_proposals
    })

def view_order(request, order_id):
    order = get_object_or_404(TransportOrder, id=order_id)
    return render(request, 'view_order.html', {'order': order})

@login_required
def accept_order(request, order_id):
    # Get the order
    order = get_object_or_404(TransportOrder, id=order_id)

    # Check if the transporter has already submitted a proposal for this order
    if TransportProposal.objects.filter(order=order, transporter=request.user).exists():
        return HttpResponse("You have already submitted a proposal for this order.")

    if request.method == 'POST':
        # Get the proposed price from the form
        price = request.POST['price']

        # Create and save the proposal
        proposal = TransportProposal(
            order=order,
            transporter=request.user,  # The logged-in transporter
            price=price,
            status='Pending'  # Proposal is pending by default
        )
        proposal.save()

        # Redirect to the transporter's dashboard or success page
        return redirect('transporter_dashboard')

    # Render the form to accept the order and submit a proposal
    return render(request, 'accept_order.html', {'order': order})


# def decline_order(request, order_id):
#     order = get_object_or_404(TransportOrder, id=order_id)
#     order.status = 'Declined'
#     order.save()
#     return redirect('transporter_dashboard')
