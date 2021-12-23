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


class Services(models.Model):
    service_title = models.CharField(max_length=200)
    service_des = models.CharField(max_length=500)
    read_more = models.CharField(max_length=20)


    def __str__(self):
        return self.service_title


class Appoinment(models.Model):
    f_name = models.CharField('First Name', max_length=50)
    l_name = models.CharField('Last Name', max_length=50)
    subject = models.CharField('Subject', max_length=120)
    appointment_date = models.DateField('Appointment Date')
    email = models.EmailField('Email')
    phone = models.IntegerField('Phone')
    message = models.TextField('Message')

    def __str__(self):
        return self.f_name+' '+self.l_name


