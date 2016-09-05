from django.contrib import admin

from proj.models import Graph, Project


@admin.register(Graph)
class GraphAdmin(admin.ModelAdmin):
    list_display = ('id', 'proj')
    list_display_links = tuple(f for f in list_display if f not in ('proj',))


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display
