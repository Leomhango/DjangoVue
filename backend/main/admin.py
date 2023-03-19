# from dataclasses import field
from django.contrib import admin

from .models import Quote

class QuoteAdmin(admin.ModelAdmin):
    fields = ('quotee', 'description')
    list_display = ('quotee', 'description', 'created_at', 'updated_at')

admin.site.register(Quote, QuoteAdmin)
