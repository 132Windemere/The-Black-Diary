from django.contrib import admin
from .models import Entrie


@admin.register(Entrie)
class EntrieAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "text",
        "image",
        "timestamp",
    ]
    search_fields = ["title", "text", "image"]
    list_filter = ["timestamp"]


admin.site.site_header = "economiicaDark Admin"
admin.site.site_title = "economiicaDark Admin"
admin.site.index_title = "Welcome to the economiicaDark Admin"
