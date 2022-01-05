from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from django.views.generic import UpdateView

from django.views.generic import CreateView

from django.views.generic import TemplateView
from .forms import Contact


# Create your views here.
def home(request):
   # return HttpResponse ("HOMEPAGE")
    return render (request,'home.html')


def education(request):
   #return HttpResponse ("education")
    return render (request,'education.html')


def projects(request):
    #return HttpResponse ("projects")
    return render (request,'projects.html')


def contact(request):
    
    #return HttpResponse ("contact")
    if request.method == 'POST':
        name = request.POST.get("name")
        companyname = request.POST.get("companyname")
        email = request.POST.get("email")
        info = request.POST.get("info")
        instance = Contact(email = email,name = name,companyname = companyname,info = info)
        instance.save()
    return render (request,'contact.html')

'''class AboutView(TemplateView):
    template_name = "contact.html"'''



