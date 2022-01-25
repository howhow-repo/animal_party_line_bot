from django.contrib import admin

from .models import TeddyStatus


class TeddyStatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TeddyStatus._meta.fields]


admin.site.register(TeddyStatus, TeddyStatusAdmin)
