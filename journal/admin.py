from django.contrib import admin

# Register your models here.

from .models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
     list_display = ['currency_pair', 'type_of_trade', 'result', 'date', 'entry_time']
     search_fields = ['result', 'currency_pair']
