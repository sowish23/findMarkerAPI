from .models import ImageUploadModel
from rest_framework import serializers


class ImgSerializer(serializers.HyperlinkedModelSerializer):
    document = serializers.ImageField(use_url=True)

    class Meta:
        model = ImageUploadModel
        fields = '__all__'