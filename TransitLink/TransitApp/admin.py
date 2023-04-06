from django.contrib import admin
from .models import Category, Location, Bus, Schedule, Booking

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Bus)
admin.site.register(Schedule)
admin.site.register(Booking)