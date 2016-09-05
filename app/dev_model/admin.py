from django.contrib import admin

from dev_model import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Dev)
class DevAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DevModel)
class DevModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ModelTag)
class ModelTagAdmin(admin.ModelAdmin):
    pass
