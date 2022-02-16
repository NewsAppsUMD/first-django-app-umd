from django.contrib import admin
from expenses.models import Summary, Detail

class SummaryAdmin(admin.ModelAdmin):
    list_display = ("office", "program", "category", "amount")
    list_filter = ("category", "program")
    search_fields = ("program",)

class DetailAdmin(admin.ModelAdmin):
    list_display = ("office", "program", "category", "payee", "purpose", "amount")
    list_filter = ("category", "program", "purpose")
    search_fields = ("program", "payee")

admin.site.register(Summary, SummaryAdmin)
admin.site.register(Detail, DetailAdmin)
