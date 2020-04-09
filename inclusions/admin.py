from django.contrib import admin
from .models import Patient, Pathology, Organ, Inclusion

admin.site.register(Patient)
admin.site.register(Pathology)
admin.site.register(Organ)
admin.site.register(Inclusion)
