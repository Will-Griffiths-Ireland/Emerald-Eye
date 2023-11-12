from django import forms
from django.contrib.auth.models import User
from django_currentuser.middleware import get_current_user
from .models import Artwork


class ArtForm(forms.ModelForm):
    """
        Form to enter a page in the journal
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['is_public'].initial = self.get_pub_pref()


    class Meta:
        model = Artwork
        fields = ['title',
                  'price',
                  'available',
                  'preview_image',
                  'full_quality_image']

        labels = {
            'title': 'Title',
            'price': 'Price',
            'available': 'Available for purchase',
            'preview_image': 'Preview Image',
            'full_quality_image': 'Image sent on purchase'
        }