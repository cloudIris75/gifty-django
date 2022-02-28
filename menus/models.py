from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=30)
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name
