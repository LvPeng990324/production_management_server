from django.contrib import admin
from Order.models import Order


@admin.register(Order)
class OrderInformation(admin.ModelAdmin):
    list_display = (
        'order_num',
        'order_status',
    )
