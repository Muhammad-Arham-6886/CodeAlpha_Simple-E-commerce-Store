from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'city', 'status', 'created_at', 'total_amount']
    list_filter = ['status', 'created_at', 'updated_at']
    list_editable = ['status']
    search_fields = ['first_name', 'last_name', 'email']
    inlines = [OrderItemInline]
