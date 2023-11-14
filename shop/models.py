from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# Artwork model

class Artwork(models.Model):
    """
    A model for each artwork
    """

    title = models.CharField(max_length=30, null=False, blank=False)
    artist_name = models.CharField(max_length=30, null=False, blank=False, default='Unknown')
    price = models.FloatField()
    sales = models.BigIntegerField(null=False, blank=False, default=0)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True, null=False, blank=False)
    available = models.BooleanField(null=False, blank=False)
    preview_image = ResizedImageField(
        size=[800, None],
        quality=80,
        upload_to="preview_images/",
        force_format="WEBP",
        null=False,
        blank=False,
    )
    full_quality_image = ResizedImageField(
        quality=100,
        upload_to="full_quality_images/",
        force_format="JPEG",
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return str(self.id)

# Orders model

class Order(models.Model):
    """
    A model for each order
    """

    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateField(auto_now_add=True, null=False, blank=False)
    complete = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    """
    A model for all the items in an order
    """

    item = models.ForeignKey(Artwork, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)




