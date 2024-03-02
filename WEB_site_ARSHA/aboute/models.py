from django.db import models
# Create your models here.
class Abaute_us(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    decspritions_1 = models.TextField(blank=True)
    decspritions_2 = models.TextField(blank=True)
    decspritions_3 = models.TextField(blank=True)
    decspritions_4 = models.TextField(blank=True)
    
    def __str__(self):
        return self.name