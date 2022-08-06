from django.shortcuts import render

from destinations.models import Day, Destination
from main.models import Equipment, EquipmentType, Photo

# Create your views here.
def homeView(request):
    template_name = 'main/home.html'
    destinations = Destination.objects.all()
    context = {
        "destinations": destinations
    }
    return render(request, template_name, context)

def bookingView(request):
    template_name = 'main/booking.html'
    context = {}
    return render(request, template_name, context)

def equipmentView(request):
    template_name = 'main/equipment.html'
    types = EquipmentType.objects.all()
    context = {
        "types": types
    }
    return render(request, template_name, context)

def galleryView(request):
    template_name = 'main/gallery.html'
    photos = Photo.objects.all()
    context = {
        "photos": photos
    }
    return render(request, template_name, context)

def error404View(request, exception):
    return render(request, '404.html')
