from django.db import models

# Create your models here.
class Input(models.Model):
    inp = models.CharField(max_length=100)

    def __str__(self):
        return self.inp