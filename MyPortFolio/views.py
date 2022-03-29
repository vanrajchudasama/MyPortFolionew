from django.shortcuts import render,HttpResponseRedirect
from .models import Contact_Us
from django.contrib import messages
# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact_Us.objects.create(name=name,email=email,subject=subject,message=message)
        messages.add_message(request,messages.INFO,'Successfully Send Message...!')   
    return HttpResponseRedirect('/')