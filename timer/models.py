from django.db import models

# Create your models here.
class Timer(models.Model):
    time_field = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
