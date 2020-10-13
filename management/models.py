from django.db import models
from django.contrib.auth.models import User
import django
# Create your models here.

class CityData(models.Model):
    city_name = models.CharField('City Name',max_length=300,blank=True)
    lat = models.FloatField('Lattitude',blank=True,default=0.0000)
    lon = models.FloatField('Longitude',blank=True,default=0.0000)

    def __str__(self):
        return self.city_name
    
    class Meta:
        verbose_name = 'Cities'
        verbose_name_plural = 'Cities'


class Category(models.Model):
    name = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class MiniLocation(models.Model):
    main_city = models.ForeignKey(CityData,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, blank=False)
    lat = models.FloatField('Latitude')
    lon = models.FloatField('Longitude')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Mini Locations'
        verbose_name_plural = 'Mini Locations'


class StateData(models.Model):
    state_name = models.CharField('State Name', max_length=300, blank=False)
    cities = models.ManyToManyField(CityData)

    def __str__(self):
        return self.state_name
    
    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'State'


class Files(models.Model):
    city = models.ManyToManyField(CityData)
    MiniLocation = models.ManyToManyField(MiniLocation)
    user = models.ForeignKey(User,limit_choices_to={'is_staff': True}, on_delete = models.CASCADE)
    company_name = models.CharField(max_length=300,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    heading = models.CharField('Heading', max_length=300)
    phone_number = models.CharField('Phone Number', max_length=1000)
    whatsapp_link = models.URLField('Whatsapp URL', max_length=1000, blank=True)
    img = models.ImageField(upload_to='img/', blank=False)
    location = models.URLField('Google Location URL', max_length=50000, blank=True)
    date = models.DateField(default=django.utils.timezone.now)
    active = models.BooleanField(default=False)
    activated_till = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.heading
    
    class Meta:
        verbose_name = 'Offers'
        verbose_name_plural = 'Offers'


class Address(models.Model):
    address = models.CharField('Address', max_length=1000,blank=False)
    mail = models.EmailField('Email Address', max_length=1000)
    phone_number = models.CharField('Phone Number', max_length=15)

    def __str__(self):
        return 'Address and Detail'
    
    class Meta:
        verbose_name = 'Address and Details'
        verbose_name_plural = 'Address and Details'


class Visitors(models.Model):
    city = models.OneToOneField(CityData, on_delete = models.CASCADE)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.city.city_name

    class Meta:
        verbose_name = 'Visitor Counts'
        verbose_name_plural = 'Visitor Counts'


class VisitCount(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return 'Counter'
    
    class Meta:
        verbose_name = 'Counter'


class Messages(models.Model):
    name = models.CharField(max_length=500,blank=False)
    email = models.EmailField(blank=False,max_length=500)
    subject = models.CharField(max_length=1000, blank=False)
    text = models.TextField()

    def __str__(self):
        return 'Message '+ str(self.id)
    
    class Meta:
        verbose_name = 'Messages'
        verbose_name_plural = 'Messages'


class WebCounter(models.Model):
    visit = models.IntegerField(default=0)

    def __str__(self):
        return 'Click to change'
    
    class Meta:
        verbose_name = 'Website Count'
        verbose_name_plural = 'Website Count'