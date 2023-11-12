from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


# Artwork model

class Artwork(models.Model):
    """
    A model for each artwork
    """

    title = models.CharField(max_length=30, null=False, blank=False)
    price = models.FloatField()
    sales = models.BigIntegerField(null=False, blank=False, default=0)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True, null=False, blank=False)
    available = models.BooleanField(null=False, blank=False)
    preview_image = ResizedImageField(
        size=[200, None],
        quality=80,
        upload_to="preview_images/",
        force_format="WEBP",
        null=True,
        blank=True,
    )
    full_quality_image = ResizedImageField(
        quality=100,
        upload_to="full_quality_images/",
        force_format="JPEG",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return str(self.id)

#id
#title
#artist_name
#description
#price

# User profile

#newletters_enabled



# Order model

#order item mode


