from django.db import models
from django.contrib.auth.models import User
import django
from datetime import date
from datetime import datetime, timedelta
from PIL import Image
from django.core.exceptions import ValidationError

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
    comes_under = models.ForeignKey(User, verbose_name='Salesperson', related_name='comes_under',on_delete=models.CASCADE)
    package_type = models.ForeignKey(PackageType, on_delete = models.CASCADE, null=True)
    change_at = models.CharField('Phamplet will change',max_length=50, choices=TIME_INTERVAL, default='5')
    city = models.ManyToManyField(CityData)
    MiniLocation = models.ManyToManyField(MiniLocation)
    user = models.ForeignKey(User,limit_choices_to={'is_staff': True}, on_delete = models.CASCADE, verbose_name="Shopkeeper")
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
    keywords = models.TextField(help_text='Provide comma-seperated keywords. Example: mobile, smartphone, charger, earphone',blank=True)
    counter = models.IntegerField(default=0)
    active_image = models.IntegerField(default=0)
    last_date = models.DateField(default=django.utils.timezone.now)
    rating = models.FloatField('Rating', default=5)
    rated_by = models.ManyToManyField(User, related_name='rated_by', blank=True)
    slider_image1 = models.ImageField('Slider Image 1',upload_to='img/', blank=True)
    slider_image2 = models.ImageField('Slider Image 2',upload_to='img/', blank=True)
    slider_image3 = models.ImageField('Slider Image 3',upload_to='img/', blank=True)

    def __str__(self):
        return str(self.id)
    
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
    end_date = models.DateTimeField(datetime.now()+timedelta(days=365))
    total_coupon = models.IntegerField(default=5)
    active = models.BooleanField(default=True)
    minimum_purchase = models.IntegerField(default=0)
    total_discount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.code)
    
    class Meta:
        verbose_name = 'Coupons'
        verbose_name_plural = 'Coupons'

class CouponHistory(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)
    is_redeemed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.status)
    
    class Meta:
        verbose_name = 'All Coupon History'
        verbose_name_plural = 'All Coupon History'

class Discount(models.Model):
    total_purchase = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.total_purchase)+":"+str(self.discount)
    
    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discount'

class ShopDetails(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    shop_name = models.CharField(max_length=1000, blank=False)
    owner_name = models.CharField(max_length=1000, blank=False)
    gst_no = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=1000, blank=False)
    whatsapp_number = models.CharField(max_length=1000, blank=False)
    address = models.CharField(max_length=1000, blank=False)
    city = models.CharField(max_length=100,blank=False)
    minilocation = models.CharField(max_length=100,blank=True)
    email_address = models.CharField(max_length=1000, blank=False)
    business_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    products = models.TextField()
    discounts = models.ManyToManyField(Discount)
    total_eligible_customer = models.IntegerField(default=0)
    package_amount = models.IntegerField(default=1)
    transaction_id = models.CharField(max_length=1000, blank=False)
    image_file1 = models.ImageField('Image 1',upload_to='img/', blank=True, null=True)
    comment1 = models.CharField(max_length=1000, blank=True)
    image_file2 = models.ImageField('Image 2',upload_to='img/', blank=True, null=True)
    comment2 = models.CharField(max_length=1000, blank=True)
    image_file3 = models.ImageField('Image 3',upload_to='img/', blank=True, null=True)
    comment3 = models.CharField(max_length=1000, blank=True)
    image_file4 = models.ImageField('Image 4',upload_to='img/', blank=True, null=True)
    comment4 = models.CharField(max_length=1000, blank=True)
    payment_verified = models.BooleanField(default=False)
    date_of_registration = models.DateField(default=django.utils.timezone.now)
    invoice_no = models.CharField(max_length=100, blank=True)
    covered_under_reward = models.BooleanField(default=False)
    covered_under_monthly_reward = models.BooleanField(default=False)
    sales_profit = models.FloatField(default=0)
    forward_to_freelancer = models.BooleanField(default=False)
    final_pamphlet = models.ImageField('Final Design', upload_to='img/', blank=True, null=True)
    design_approved = models.BooleanField(default=False)
    freelancer_profit = models.IntegerField(default=0)
    designed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="designed_by")
    latitude = models.FloatField(blank=True, default=0.0)
    longitude = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return self.shop_name

    class Meta:
        verbose_name = 'Shop Informations'
        verbose_name_plural = 'Shop Informations'

class FileTest(models.Model):
    file = models.ImageField('Image 1',upload_to='img/', blank=False, null=True)
    
    class Meta:
        verbose_name = "Testing Image File Upload"
        verbose_name_plural = "Testing Image File"

class SocialAccounts(models.Model):
    name = models.CharField(max_length=100, blank=False)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Social Accounts"
        verbose_name_plural = "Social Accounts" 

class PaymentIssue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    offer = models.ForeignKey(Files, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "Payment Complaint"

class PamphletDesign(models.Model):
    title = models.CharField('Title of Pamphlet',max_length=50, blank=True)
    message = models.CharField('Message on Pamphlet',max_length=100, blank=True, help_text="This message will get printed on the Pamphlet")
    design = models.ImageField(blank=True, upload_to='img/', null=True, help_text="Uploaded image dimention must be 750X800 pixels")
    font_file = models.FileField(blank=True)
    total_downloads = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        print("IMAGE SAVED")
        im = Image.open(self.design)
        width, height = im.size # must be 750 X 800

        if (width<745 or width>755) or (height<795 or height>805):
            raise ValidationError(('Image size must be 750 X 800'))
        
        print(width, height)
        super(PamphletDesign, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Phamplate Design"
        verbose_name_plural = "Phamplate Design"

class DownloadedDesigns(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    base_pamphlet = models.ForeignKey(PamphletDesign, on_delete=models.CASCADE, null=True)
    design = models.ImageField(blank=True, upload_to='img/', null=True)

    def __str__(self):
        return self.user.username+"'s Design"
    
    class Meta:
        verbose_name = "Downloadable Designs"
        verbose_name_plural = "Downloadable Designs"

class DefaultDesign(models.Model):
    design = models.ImageField('Default Design', upload_to='img/', blank=True, null=True)

    def __str__(self):
        return "Default Design"
    
    def save(self, *args, **kwargs):
        if len(DefaultDesign.objects.all()) > 0:
            raise ValidationError(('Only 1 default design is allowed'))
        super(DefaultDesign, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Default Design"
        verbose_name_plural = "Default Design"

class TermsCondition(models.Model):
    text = models.TextField()

    def __str__(self):
        return "Terms and Condition"
    
    class Meta:
        verbose_name = "Terms and Condition"
        verbose_name_plural = "Terms and Condition"

class EnquiryLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Files, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " on " + str(self.date) + " to " + self.shop.company_name
    
    class Meta:
        verbose_name = "Enquiry Logs"
        verbose_name_plural = "Enquiry Logs"