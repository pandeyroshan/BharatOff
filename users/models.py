from django.db import models
from django.contrib.auth.models import User
from management.models import CityData
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    city = models.ForeignKey(CityData,on_delete=models.CASCADE, null=True)
    mobile_number = models.CharField(max_length=15,blank=False)
    pwd = models.CharField(max_length=500,blank=False)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Profiles'
        verbose_name_plural = 'Profiles'