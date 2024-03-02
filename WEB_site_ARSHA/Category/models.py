from django.db import models
from django.urls import reverse
# Create your models here.
class Category_Portfolia(models.Model):
    name = models.CharField(max_length=100, unique=True)
    decspritions = models.TextField(blank=True)
    image = models.ImageField(upload_to="photo/category",blank=True)
    slug = models.SlugField(max_length=20,unique=True)
    
    def __str__(self):
        return self.name 
    
    def manzil_olmoq(self):
        return reverse("category_url", args=[self.slug])