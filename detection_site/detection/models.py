from django.db import models

# Model Detection

class Det_model(models.Model):

    title = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='detect_photo/before')
    file = models.FileField(upload_to='detect_photo/before', default=None, blank=True)

class Det_result(models.Model):

    title = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='detect_photo/after')