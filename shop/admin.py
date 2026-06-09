from django.contrib import admin
from .models import Product, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'available']
    list_filter = ['category', 'available']
    search_fields = ['name', 'description']
    list_editable = ['price', 'stock', 'available']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'status', 'total', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['full_name', 'email']
    readonly_fields = ['created_at']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']