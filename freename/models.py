from django.db import models

# Create your models here.
class FreeName(models.Model):
    name = models.CharField(max_length = 500)