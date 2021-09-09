from django.db import models

# Create your models here.
class Books(models.Model):
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    read = models.BooleanField(default=False)

