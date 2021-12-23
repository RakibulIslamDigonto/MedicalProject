from django.db import models

# Create your models here.
class SlideModel(models.Model):
    title = models.CharField(max_length=200)
    short_des = models.CharField(max_length=300)
    slide_image = models.ImageField(blank=True, upload_to='slids/')
    def __str__(self):
        return self.title

    def image_url(self):
        try:
            url=self.slide_image.url
        except:
            url=''
        return url


class Skill(models.Model):
    skill_title = models.CharField(max_length=200)
    skill_Quantity = models.IntegerField()

    def __str__(self):
        return self.skill_title

