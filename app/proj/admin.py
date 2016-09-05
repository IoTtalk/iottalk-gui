from django.contrib import admin

from proj.models import Graph, Project


@admin.register(Graph)
class GraphAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
