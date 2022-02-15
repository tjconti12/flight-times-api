from django.db import models

# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=4)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name