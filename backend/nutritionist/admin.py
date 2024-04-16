from django.contrib import admin
from .models import Patient, Nutritionist, Appointment, Event, Evaluation, Evolution, Diet

# Register your models here.
admin.site.register(Nutritionist)
admin.site.register(Appointment)
admin.site.register(Event)
admin.site.register(Patient)
admin.site.register(Evaluation)
admin.site.register(Evolution)
admin.site.register(Diet)