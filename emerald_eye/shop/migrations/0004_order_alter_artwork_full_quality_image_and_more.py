# Generated by Django 4.2.7 on 2023-11-12 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0003_alter_artwork_preview_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_ordered", models.DateField(auto_now_add=True)),
                ("complete", models.BooleanField(default=False)),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.AlterField(
            model_name="artwork",
            name="full_quality_image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                force_format="JPEG",
                keep_meta=True,
                quality=100,
                scale=None,
                size=[1920, 1080],
                upload_to="full_quality_images/",
            ),
        ),
        migrations.AlterField(
            model_name="artwork",
            name="preview_image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                force_format="WEBP",
                keep_meta=True,
                quality=80,
                scale=None,
                size=[800, None],
                upload_to="preview_images/",
            ),
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="shop.artwork",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="shop.order",
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
    ]
