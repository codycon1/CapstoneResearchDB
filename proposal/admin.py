from django.contrib import admin

# Register your models here.
from django.contrib import admin
from proposal import models

@admin.register(models.proposal)
class ProposalAdmin(admin.ModelAdmin):
    pass


