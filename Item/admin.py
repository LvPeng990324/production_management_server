from django.contrib import admin
from Item.models import Item
from Item.models import TechnicalChange


@admin.register(Item)
class ItemInformation(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(TechnicalChange)
class TechnicalChangeInformation(admin.ModelAdmin):
    list_display = (
        'name',
    )

