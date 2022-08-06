from django.urls import path

from main.views import bookingView, equipmentView, galleryView, homeView

app_name = 'main'

urlpatterns = [
    path('', homeView, name='home-view'),
    path('equipment/', equipmentView, name='equipment-view'),
    path('gallery/', galleryView, name='gallery-view'),
    path('booking/', bookingView, name='booking-view'),
]