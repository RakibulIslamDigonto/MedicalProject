from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import URLField

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



class Department(models.Model):
    dep_name = models.CharField('First Name', max_length=50)
    slug = models.SlugField(unique=True)
    dep_short_des= models.TextField(blank=True)
    dep_image = models.ImageField(upload_to='dep_images/', blank=True)

    def __str__(self):
        return self.dep_name


    def image_url(self):
        try:
            url=self.dep_image.url
        except:
            url=''
        return url

    


class Department_galary(models.Model):
    department = models.ForeignKey(Department, max_length=50, on_delete=models.CASCADE, related_name='dep_gal')
    dep_title = models.CharField(max_length=100)
    dep_sub_title= models.CharField(max_length=500)
    dep_image = models.ImageField(upload_to='dep_images/', blank=True)

    def __str__(self):
        return self.dep_title


    def image_url(self):
        try:
            url=self.dep_image.url
        except:
            url=''
        return url


class Schedule(models.Model):
    day= models.CharField(max_length=50)
    time= models.CharField(max_length=50)
    def __str__(self):
        return self.day


class Doctor(models.Model):
    doc_name = models.CharField(max_length=150)
    doc_image = models.ImageField(upload_to='dep_images/', blank=True)
    doc_designation= models.CharField(max_length=50)
    fb_link= models.URLField(max_length=254, blank=True)
    tw_link= models.URLField(max_length=254, blank=True)
    li_link= models.URLField(max_length=254, blank=True)
    doc_schedule= models.ManyToManyField(Schedule, related_name='doct_schedule')


    def __str__(self):
        return self.doc_name


    def image_url(self):
        try:
            url=self.doc_image.url
        except:
            url=''
        return url



class ServicesCount(models.Model):
    service_count = models.IntegerField('Service Count')
    services_title = models.CharField('Service', max_length=50)
    def __str__(self):
        return self.services_title



class Clint_feedback(models.Model):
    cli_name = models.CharField('Client Name', max_length=50)
    cli_designation = models.CharField('Client Designation', max_length=50)
    cli_feedback= models.TextField()
    cli_image = models.ImageField(upload_to='dep_images/', blank=True)

    def __str__(self):
        return self.cli_name


    def image_url(self):
        try:
            url=self.cli_image.url
        except:
            url=''
        return url

