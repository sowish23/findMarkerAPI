from django.db import models
from django.core.files import File
import urllib
import os

class ImageUploadModel(models.Model):
    document = models.ImageField(upload_to = 'images', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # def get_remote_image(self):
    #     if self.document_url and not self.document:
    #         result = urllib.urlretrieve(self.document_url)
    #         self.document.save(
    #                 os.path.basename(self.document_url),
    #                 File(open(result[0]))
    #                 )
    #         self.save()

class Address(models.Model):
    document = models.ImageField(upload_to = 'images', blank=True, null=True)
    address = models.TextField(null = True)
