from django.contrib import admin

from .models import Event

# @admin.site.register(Event)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'datetime', 'priority']
    list_filter = ['status']
