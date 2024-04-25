
from django.shortcuts import render

def homepage(request):
    return render(request, 'portfolio/homepage.html')

def about(request):
    return render(request, 'portfolio/about.html')

def services(request):
    return render(request, 'portfolio/services.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
