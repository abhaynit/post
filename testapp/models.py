from django.db import models

# Create your models here.
class addimg(models.Model):
    im = models.ImageField(upload_to = "media")

class addimg1(models.Model):
    im = models.ImageField(upload_to = "media")
    is_pri = models.BooleanField(default=False)
