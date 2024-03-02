from django.db import models
from Category.models import *
# Create your models here.
class Portfolia(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=199)
    descpritions = models.TextField(blank=True)
    xozirgi_narx = models.IntegerField()
    oldingi_narx = models.IntegerField()
    created_one = models.DateTimeField(auto_now_add=True)
    categpory = models.ForeignKey(Category_Portfolia,on_delete=models.CASCADE)
    mavjudmi = models.BooleanField(default=True)
    slug = models.SlugField(max_length=20,unique=True)


    def __str__(self):
        return self.name

class Services(models.Model):
    img = models.ImageField(upload_to="services/")
    name = models.CharField(max_length=200)
    descrition = models.TextField()

    def __str__(self):
        return self.name