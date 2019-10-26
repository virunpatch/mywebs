from django.db import models

# Create your models here.
class Service(models.Model):
    icon = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    detail = models.CharField(max_length=1000)

    def __str__(self):
        return self.title