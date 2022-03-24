from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("projectTitle", "projectAuthor",)


admin.site.register(Project, ProjectAdmin)
