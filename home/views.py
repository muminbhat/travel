from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Packages

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(name=name, email=email, message=message)
        contact.save()

    packages = Packages.objects.all()
    context = {'packages':packages}

    return render(request, 'index.html', context)

def package(request, slug):
    package = Packages.objects.filter(slug=slug)
    context = {'package':package}
    

    return render(request, "packages.html", context)
