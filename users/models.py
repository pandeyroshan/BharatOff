from django.db import models
from django.contrib.auth.models import User
from management.models import CityData
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15,blank=False)
    pwd = models.CharField(max_length=500,blank=False)
    otp = models.IntegerField(default=0)
    is_varified = models.BooleanField(default=False)

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
    otp = models.IntegerField(default=0)
    is_varified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Shopkeepers Profile'
        verbose_name_plural = 'Shopkeepers Profile'


class SalesPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15, blank=False)
    pwd = models.CharField('Password', max_length=1000, blank=False)
    city = models.ForeignKey(CityData, blank=True, on_delete=models.CASCADE)
    otp = models.IntegerField(default=0)
    is_varified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Sales Person'
        verbose_name_plural = 'Sales Person'

class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15, blank=False)
    pwd = models.CharField('Password', max_length=1000, blank=False)
    comes_under = models.OneToOneField(SalesPerson, on_delete = models.CASCADE, null=True)
    otp = models.IntegerField(default=0)
    is_varified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Freelancer Profile'
        verbose_name_plural = 'Freelancer Profile'
