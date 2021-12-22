from django.db import models

# Create your models here.
class SlideModel(models.Model):
    title = models.CharField(max_length=200)
    short_des = models.CharField(max_length=300)
    slide_image = models.ImageField(blank=True)
    def __str__(self):
        return self.title




    
