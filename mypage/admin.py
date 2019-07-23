from django.contrib import admin

# Register your models here.
from .models import cdetails, ldetails

admin.site.register(cdetails)
admin.site.register(ldetails)