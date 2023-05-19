from django.db import models
from django.db import models

class Togri(models.Model):
    soz = models.CharField(max_length=100)
    def __str__(self):
        return self.soz

class Natogri(models.Model):
    soz = models.CharField(max_length=100)
    t_soz = models.ForeignKey(Togri, on_delete=models.CASCADE)
    def __str__(self):
        return self.soz

# Create your models here.
