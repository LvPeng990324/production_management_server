from django.contrib import admin
from Supplier.models import Supplier


@admin.register(Supplier)
class SupplierInformation(admin.ModelAdmin):
    list_display = (
        'name',
    )
