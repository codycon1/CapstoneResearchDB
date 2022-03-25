import django.contrib.auth.admin
from django.contrib import admin

from users.models import RUser


@admin.register(RUser)
class UserAdmin(django.contrib.auth.admin.UserAdmin):
    fieldsets = (
        (None, {'fields': (
            'first_name', 'last_name', 'email', 'password', 'is_active', 'is_staff',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password', 'is_active', 'is_staff',)}),
    )
    # exclude = ['username',]
    ordering = ('email',)
    list_display = ['email', 'first_name', 'last_name', ]
