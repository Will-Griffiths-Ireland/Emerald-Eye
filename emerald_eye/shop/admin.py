from django.contrib import admin
from .models import Artwork, Order, OrderItem

# Register your models here.

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        'artist_name',
        "price",
        "available",
    )
    list_filter = ("artist_name", "date_added")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        'date_ordered',
        "complete",
    )
    list_filter = ("customer", "date_ordered")

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        'item',
    )
    list_filter = ("order", "item")