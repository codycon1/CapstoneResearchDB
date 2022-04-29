from django.contrib import admin

from .models import Project, ProjectFile

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "projectTitle", "projectAuthor",]


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ["projectID", "userEmail", "type", "uploadDate"]

