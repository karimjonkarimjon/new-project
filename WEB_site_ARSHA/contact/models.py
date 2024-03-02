from django.db import models

# Create your models here.

class contact(models.Model):
    your_name = models.CharField(max_length=30)
    your_email = models.EmailField()
    your_msg = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.your_name