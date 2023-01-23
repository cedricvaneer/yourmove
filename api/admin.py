from django.contrib import admin

# Register your models here.
from base.models import Customer, VehicleType, Vehicle, Booking

admin.site.register(Customer)
admin.site.register(VehicleType)
admin.site.register(Vehicle)
admin.site.register(Booking)
