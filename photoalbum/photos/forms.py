from django.forms import ModelForm
from .models import PhotoGallery


class AddPhoto(ModelForm):
    class Meta:
        model = PhotoGallery
