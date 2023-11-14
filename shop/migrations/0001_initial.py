# Generated by Django 3.2.23 on 2023-11-12 14:19

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('sales', models.BigIntegerField(default=0)),
                ('description', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('available', models.BooleanField()),
                ('preview_image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=80, scale=None, size=[200, None], upload_to='preview_images/')),
                ('full_quality_image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='full_quality_images/')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]