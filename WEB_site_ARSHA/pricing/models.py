from django.db import models

# Create your models here.
class Pricing(models.Model):
    name = models.CharField(max_length=30)
    narx = models.IntegerField()
    descpritions_1 = models.TextField(blank=True)
    descpritions_2 = models.TextField(blank=True)
    descpritions_3 = models.TextField(blank=True)
    descpritions_4 = models.TextField(blank=True)
    descpritions_5 = models.TextField(blank=True)
    
    def __str__(self):
        return self.name