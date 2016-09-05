from django.contrib import admin

from dev_model import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display


@admin.register(models.Dev)
class DevAdmin(admin.ModelAdmin):
    list_display = ('id', 'mod', 'type', 'graph')
    list_display_links = list_display


@admin.register(models.DevModel)
class DevModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display


@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'type', 'cate', 'func')
    list_display_links = ('id', 'name', 'type')


@admin.register(models.ModelTag)
class ModelTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display
