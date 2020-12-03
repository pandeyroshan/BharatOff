from django.db import models
from django.contrib.auth.models import User
from management.models import CityData
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15,blank=False)
    pwd = models.CharField(max_length=500,blank=False)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'All Profiles'
        verbose_name_plural = 'All Profiles'

class Shopkeeper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15, blank=False)
    pwd = models.CharField('Password', max_length=1000, blank=False)
    city = models.ForeignKey(CityData, blank=True, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    notification = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Shopkeepers Profile'
        verbose_name_plural = 'Shopkeepers Profile'

class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15, blank=False)
    pwd = models.CharField('Password', max_length=1000, blank=False)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Freelancer Profile'
        verbose_name_plural = 'Freelancer Profile'