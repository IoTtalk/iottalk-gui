from django.contrib import admin

from user_func.models import FeatureFunc, JoinFunc


@admin.register(FeatureFunc)
class FeatureFuncAdmin(admin.ModelAdmin):
    pass


@admin.register(JoinFunc)
class JoinFuncAdmin(admin.ModelAdmin):
    pass
