from django.db import models

# Create your models here.
class Books(models.Model):
    image = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    description = models.TextField(max_length=1000, blank=True, null=True)
    read = models.BooleanField(default=False, blank=True)

