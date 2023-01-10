from django.shortcuts import render
from .models import Project, Contact
from django.contrib import messages
from django.http import HttpResponseRedirect
import pyshorteners

# Create your views here.

def index(request):
    projects=Project.objects.all()
    if request.method=="POST" and 'link' in request.POST:
        link = request.POST['link']
        print(link)
        short = pyshorteners.Shortener()
        x = short.tinyurl.short(link)
        messages.success(request,'Here is the short url:  '+x)
        return HttpResponseRedirect('/')

    if request.method=="POST" and 'contact`' in request.POST:
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact = Contact.objects.create(name=name,email=email,
        subject=subject,message=message)
        contact.save()
        messages.success(request, 'Message successfully sent')
        return HttpResponseRedirect('/')

    return render(request, 'index.html',{'projects':projects})
