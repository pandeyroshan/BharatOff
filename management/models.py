from django.db import models
from django.contrib.auth.models import User
import django

CHOICES_CATEGORY = [
    ('1' , 'Fashion'),
    ('2' , 'Property'),
    ('3' , 'Electronics'),
    ('4' , 'Food & Restaurant'),
    ('5' , 'Supermarket'),
    ('6' , 'Service'),
]

TIME_INTERVAL = [
    ('0', 'Twice a day'),
    ('1', 'Daily'),
    ('2', 'Weekly'),
    ('3', 'Fortnight'),
    ('4', 'Monthly'),
    ('5', 'I will handle')
]


class PackageType(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.IntegerField(default=0)
    total_phamplet = models.IntegerField(default=0)
    total_videos = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Packages'
        verbose_name_plural = 'Packages'

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
    img = models.ImageField('Image',upload_to='img/', blank=True)

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
    cities = models.ManyToManyField(CityData, blank=True)

    def __str__(self):
        return self.state_name
    
    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'State'


class Files(models.Model):
    package_type = models.ForeignKey(PackageType, on_delete = models.CASCADE)
    change_at = models.CharField('Phamplet will change',max_length=50, choices=TIME_INTERVAL, default='5')
    city = models.ManyToManyField(CityData)
    MiniLocation = models.ManyToManyField(MiniLocation)
    user = models.ForeignKey(User,limit_choices_to={'is_staff': True}, on_delete = models.CASCADE)
    company_name = models.CharField(max_length=300,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    icon_category = models.CharField(max_length=50, choices=CHOICES_CATEGORY, default="1")
    heading = models.CharField('Heading', max_length=300)
    phone_number = models.CharField('Phone Number', max_length=1000)
    whatsapp_link = models.URLField('Whatsapp URL', max_length=1000, blank=True)
    img = models.ImageField('Image 1',upload_to='img/', blank=False)
    img1 = models.ImageField('Image 2',upload_to='img/', blank=True)
    img2 = models.ImageField('Image 3',upload_to='img/', blank=True)
    img3 = models.ImageField('Image 4',upload_to='img/', blank=True)
    img4 = models.ImageField('Image 5',upload_to='img/', blank=True)
    img5 = models.ImageField('Image 6',upload_to='img/', blank=True)
    img6 = models.ImageField('Image 7',upload_to='img/', blank=True)
    img7 = models.ImageField('Image 8',upload_to='img/', blank=True)
    img8 = models.ImageField('Image 9',upload_to='img/', blank=True)
    img9 = models.ImageField('Image 10',upload_to='img/', blank=True)
    location = models.URLField('Google Location URL', max_length=50000, blank=True)
    date = models.DateField(default=django.utils.timezone.now)
    active = models.BooleanField(default=False)
    activated_till = models.DateField(default=django.utils.timezone.now)
    facebook_link = models.URLField('Facebook Link',max_length=2000, blank=True)
    instagram_link = models.URLField('Instagram Link',max_length=2000, blank=True)
    youtube_link = models.URLField('Youtube Link',max_length=2000, blank=True)
    keywords = models.TextField(blank=True)
    counter = models.IntegerField(default=0)
    active_image = models.IntegerField(default=0)
    last_date = models.DateField(default=django.utils.timezone.now)
    rating = models.FloatField('Rating', default=5)
    rated_by = models.ManyToManyField(User, related_name='rated_by', blank=True)

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

class MarketingSources(models.Model):
    source = models.CharField(max_length=200, blank=False)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.source
    
    class Meta:
        verbose_name = 'Marketing Sources'
        verbose_name_plural = 'Marketing Sources'

class Resources(models.Model):
    img = models.ImageField('Image 1',upload_to='img/', blank=False)
    code = models.CharField('Codeword', max_length=50, unique=True)
    keyword = models.TextField()

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = 'Image Resources'
        verbose_name_plural = 'Image Resources'
    

class Coupon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Shopkeeper
    code = models.CharField(max_length=10, blank=False)
    offer = models.ForeignKey(Files, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    total_coupon = models.IntegerField(default=5)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.code)
    
    class Meta:
        verbose_name = 'Coupons'
        verbose_name_plural = 'Coupons'

class CouponHistory(models.Model):
    code = models.CharField(max_length=10, blank=True)
    ad = models.ForeignKey(Files, on_delete = models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.BooleanField()
    timestamp = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.status)
    
    def varify(self, coupon_id, user_id):
        if CouponHistory.objects.all().filter(coupon = Coupon.objects.get(id = int(coupon_id)), user = User.objects.get(id = int(user_id))):
            context = {}
            context['coupon'] = Coupon.objects.get(id = int(coupon_id))
            coupon_history = CouponHistory.objects.all().filter(coupon = Coupon.objects.get(id = int(coupon_id)), user = User.objects.get(id = int(user_id)))[0]
            context['status'] = coupon_history.status
            return context
    
    class Meta:
        verbose_name = 'All Coupon History'
        verbose_name_plural = 'All Coupon History'