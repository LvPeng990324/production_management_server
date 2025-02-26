from django.contrib import admin
from UserManagement.models import User


@admin.register(User)
class UserInformation(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
    )

