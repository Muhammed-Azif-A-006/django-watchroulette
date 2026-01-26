from django.contrib import admin

from .models import WatchItem

@admin.register(WatchItem)
class WatchItemAdmin(admin.ModelAdmin):
    list_display = ("title", "item_type", "watched", "rating", "added_by", "created_at")
    list_filter = ("item_type", "watched")
    search_fields = ("title", "genre", "notes")
