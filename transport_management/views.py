# transport_management/views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'index.html')




def vendor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('vendor_dashboard'))  # Redirect to vendor dashboard
    return render(request, 'vendor_login.html')


def transporter_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('transporter_dashboard'))  # Redirect to transporter dashboard
    return render(request, 'transporter_login.html')
