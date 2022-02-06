from django.contrib import admin
from funwithmodels import models


# Register your models here.
@admin.register(models.CommonDataTypes)
class CommonAdmin(admin.ModelAdmin):
    list_display = ['binary', 'bool', 'str', 'float', 'int', 'date', 'time']


@admin.register(models.FKModel)
class FKAdmin(admin.ModelAdmin):
    list_display = ['foreignkey',]