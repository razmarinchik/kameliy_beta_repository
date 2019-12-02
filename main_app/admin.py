from django.contrib import admin
from .models import Master, Service, FreeTime, Records

admin.site.register(Master)
admin.site.register(Service)
admin.site.register(FreeTime)
admin.site.register(Records)

# Register your models here.
