from django.db import models

from destinations.models import Cartegory, Itinerary

# Create your models here.
class EquipmentType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'Equipment Type'
        verbose_name_plural = ' Types of Equipments'

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(EquipmentType, on_delete=models.SET_NULL, related_name='equipments', blank=True, null=True)
    image = models.ImageField()
    price = models.CharField(max_length=10)
    description = models.TextField()

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return 'Photo'


class FeaturedTour(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='featured_itineraries')

    class Meta:
        verbose_name = 'Featured Tour'
        verbose_name_plural = 'Featured Tours'

    def __str__(self):
        return self.itinerary.name


class FeaturedCartegory(models.Model):
    cartegory = models.ForeignKey(Cartegory, on_delete=models.CASCADE, related_name='featured_itineraries')

    class Meta:
        verbose_name = 'Featured Cartegory'
        verbose_name_plural = 'Featured Cartegories'

    def __str__(self):
        return self.cartegory.name

