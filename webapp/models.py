from django.db import models

class ImageUploadModel(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
