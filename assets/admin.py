from django.contrib import admin

# Register your models here.
from .models import Asset, Purchase

admin.site.register(Purchase)
admin.site.register(Asset)