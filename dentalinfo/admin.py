from django.contrib import admin
from .models import Service, Patient, Dentist, Year, Month, Day, Hour, Time, Appointment

# Register your models here.
admin.site.register(Service)
admin.site.register(Patient)
admin.site.register(Dentist)
admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Day)
admin.site.register(Hour)
admin.site.register(Time)
admin.site.register(Appointment)

