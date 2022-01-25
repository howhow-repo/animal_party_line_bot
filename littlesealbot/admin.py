from django.contrib import admin

from .models import LittleSealStatus


class LittleSealStatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LittleSealStatus._meta.fields]

admin.site.register(LittleSealStatus, LittleSealStatusAdmin)
