from django.db import models
from Category.models import *
# Create your models here.
class Add_Team(models.Model):
    image = models.ImageField(upload_to="add_product/")
    name = models.CharField(max_length=50)
    what_work = models.CharField(max_length=200)
    decpritions = models.TextField()
    twiter = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name
    

