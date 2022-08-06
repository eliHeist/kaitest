from django.contrib import admin

from destinations.models import Cartegory, Day, Destination, Itinerary

# Register your models here.
admin.site.register(Destination)
admin.site.register(Cartegory)

class InlineDay(admin.StackedInline):
    model = Day
    extra = 1
    show_change_link = True
    can_delete = True


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    inlines = [InlineDay]
