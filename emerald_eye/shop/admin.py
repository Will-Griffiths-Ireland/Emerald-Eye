from django.contrib import admin
from .models import Artwork

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
