from django.db import models
from django.contrib.auth.models import User
from management.models import CityData
import django
from management.models import ShopDetails, MiniLocation
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15,blank=False)
    pwd = models.CharField(max_length=500,blank=False)
    otp = models.IntegerField(default=0)
    is_varified = models.BooleanField(default=False)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'All Profiles'
        verbose_name_plural = 'All Profiles'

class Shopkeeper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15, blank=False)
    email = models.EmailField(blank=True)
    pwd = models.CharField('Password', max_length=1000, blank=False)
    city = models.ForeignKey(CityData, blank=True, on_delete=models.CASCADE, null=True)
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
    email = models.EmailField(blank=True)
    pwd = models.CharField('Password', max_length=1000, blank=False)
    city = models.ForeignKey(CityData, blank=True, on_delete=models.CASCADE)
    otp = models.IntegerField(default=0)
    is_varified = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    suspend_account = models.BooleanField(default=False)
    can_change_photo = models.BooleanField('Can Change Photo', default=False)
    share = models.IntegerField(default=0)
    security_code = models.CharField(max_length=4,blank=True)
    security_warning = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Sales Person'
        verbose_name_plural = 'Sales Person'

class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    mobile_number = models.CharField(max_length=15, blank=False)
    pwd = models.CharField('Password', max_length=1000, blank=False)
    comes_under = models.ManyToManyField(SalesPerson)
    otp = models.IntegerField(default=0)
    is_varified = models.BooleanField(default=False)
    per_design_profit = models.IntegerField('Per Design Cost',default=0)
    date_of_joining = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Freelancer Profile'
        verbose_name_plural = 'Freelancer Profile'

class CustomerLogin(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    password = models.CharField(max_length=15, blank=False)
    mobile = models.CharField(max_length=15, default='XXXXXXXXXX')
    otp = models.IntegerField(default=0)
    is_varified = models.BooleanField(default=False)
    coupon_code = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = 'Customer Login Info'
        verbose_name_plural = 'Customer Login Info'

class RewardScheme(models.Model):
    package = models.IntegerField(default=0, blank=False)
    total_sale = models.IntegerField(default=0, blank=False)
    time = models.IntegerField('Time Duration in Days',default=0, blank=False)
    total_rewards = models.IntegerField('Reward', default=0, blank=False)

    def __str__(self):
        return "Reward on "+str(self.package)
    
    class Meta:
        verbose_name = "Reward Scheme"
        verbose_name_plural = "Reward Scheme"

class RewardHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.CharField(max_length=1000, blank=False)
    date = models.DateField(default=django.utils.timezone.now)
    reward = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username+"'s Reward"
    
    class Meta:
        verbose_name = "Reward History"
        verbose_name_plural = "Reward History"

class FreelancerEarning(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=django.utils.timezone.now)
    note = models.CharField(max_length=1000, blank=True)
    earning = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.freelancer.user.username+"'s Earning"

class Designcomments(models.Model):
    shopdetails = models.ForeignKey(ShopDetails, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=django.utils.timezone.now)
    comment = models.CharField(max_length=3000, blank=False)

    class Meta:
        verbose_name = "Design Comments"
        verbose_name_plural = "Design Comments"

class NotificationAlert(models.Model):
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    # shopkeeper's user
    text = models.CharField(max_length=1000, blank=False) 
    timestamp = models.DateField(default=django.utils.timezone.now)                       # Time when this gets created
    minilocations = models.ManyToManyField(MiniLocation)                       # minilocation coverage
    total_reach = models.IntegerField(default=0)                              # Total views/delivery

    class Meta:
        verbose_name = "Notifications"
        verbose_name_plural = "Notifications"

class UserNotification(models.Model):
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    notification_text = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return str(self.target_user.username)+"'s Notifiction"
    
    class Meta:
        verbose_name = "Users Notification"
        verbose_name_plural = "Users Notification"

class DeviceID(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=2000, blank=False)

    def __str__(self):
        return "Device "+str(self.user.username)
    
    class Meta:
        verbose_name = "Device IDs"
        verbose_name_plural = "Device IDs"
    
class MonthlyWinner(models.Model):
    monthYear = models.CharField(max_length=20)
    prize = models.CharField(max_length=100, blank=True)
    customers = models.ManyToManyField(CustomerLogin)

    def __str__(self):
        return self.monthYear
    
    class Meta:
        verbose_name = "Monthly Winners"
        verbose_name_plural = "Monthly Winners"