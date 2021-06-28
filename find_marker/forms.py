from .models import ImageUploadModel
from django import forms

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ('document', )