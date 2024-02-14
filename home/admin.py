from django.contrib import admin
from .models import (SnapShopOrders, DartilOrders)

class SnapShopOrdersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'corp_order_code', 'order_code', 'pdf_file', 'order_status', 'send_status', 'price')
    list_filter = ('order_status', 'send_status', 'product_created_at', 'product_updated_at',)
    search_fields = ('full_name', 'corp_order_code', 'order_code', 'pdf_file', 'order_status', 'send_status')

class DartilOrdersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'corp_order_code', 'order_status', 'price', 'pdf_file', )
    list_filter = ('order_status', 'product_created_at', 'product_updated_at', )
    search_fields = ('full_name', 'corp_order_code', 'order_status', 'price', 'pdf_file', )

admin.site.register(SnapShopOrders, SnapShopOrdersAdmin)

admin.site.register(DartilOrders, DartilOrdersAdmin)