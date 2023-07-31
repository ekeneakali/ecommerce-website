
from django.db import models

from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from djmoney.models.fields import MoneyField

from django_countries.fields import CountryField

import uuid
from address.models import AddressField

from djmoney.models.managers import money_manager

from django.contrib.auth.models import AbstractUser

from django.apps import AppConfig


# Create your models here.


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'frontend'

# class Account(models.Model):
#     choose = models.CharField(max_length=1000)

#     def __str__(self):
#         return self.choose

#     class Meta():
#         verbose_name_plural = 'Account'


# class MyUser(AbstractUser):
   
#     account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='select account')

#     class Meta():
#         verbose_name_plural = 'MyUser'



class Discount(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Discount'



class Category(models.Model):
    select = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.select

    class Meta():
        verbose_name_plural = 'Category'

class Select_Category(models.Model):
    select = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.select

    class Meta():
        verbose_name_plural = 'Select Category'

class Payment(models.Model):
    

    name = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    class Meta():

        verbose_name_plural = 'Payment'

class Details(models.Model):
    

    name = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    class Meta():

        verbose_name_plural = 'Detail'

class Delivery(models.Model):
    

    name = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    class Meta():

        verbose_name_plural = 'Delivery'





class Product(models.Model):
    government = models.FileField(upload_to='government_id/', verbose_name='upload your government id or business license')
    name = models.CharField(max_length=150, verbose_name='name of product')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, verbose_name='select payment')
    price = models.IntegerField()
    old = models.IntegerField(blank=True, null=True, verbose_name='old price(optional)')
    new_price = models.CharField(max_length=1000)
    old_price = models.CharField(max_length=1000, blank=True, null=True, verbose_name='old price(optional)')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=50, verbose_name='company name')
    select_category = models.ForeignKey(Select_Category, on_delete=models.CASCADE)
    supply = models.IntegerField(verbose_name='supply quantity')
    detail = models.ForeignKey(Details, on_delete=models.CASCADE, verbose_name='select packaging details')
    country = models.CharField(verbose_name='your country')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='select business type')
    phone_number = PhoneNumberField(verbose_name='phonenumber (country code first)')
    email = models.EmailField()
    country = CountryField()
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, verbose_name='select delivery time')
    size = models.IntegerField(default=0)
    cost = models.IntegerField(default=0, verbose_name='shipping cost')
    num_site = models.IntegerField(default=0, verbose_name='visited')
    video= models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name='upload a video(optional)')
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True, verbose_name='select discount(optional)')
    description = models.TextField()
    image = models.FileField(upload_to='upload/', verbose_name='upload a photo')
    thumbnail = models.FileField(upload_to='thumbnail/', verbose_name='upload a photo')
    multiple = models.FileField(upload_to='multiple/', verbose_name='upload a photo')
    img_view = models.FileField(upload_to='img_view/', verbose_name='upload a photo')
    img_slider = models.FileField(upload_to='img_slider/', verbose_name='upload a photo')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def total_likes(self):
        return self.likes.count()

    class Meta():
        verbose_name_plural = 'Product'

    
    class Meta():

        ordering = ['-created_at',]

class Select(models.Model):
    CHOICES = (
    ('select1', 'seller'),
    ('select2', 'buyer'),
    ('select3', 'seller/buyer'),


)

    select = models.CharField(max_length=1000, choices=CHOICES, verbose_name='select account')
    phone_number = PhoneNumberField(verbose_name='phonenumber (country code first)')
    country = CountryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.select
    
    class Meta():

        verbose_name_plural = 'Select'

class SellersAccount(models.Model):
    image = models.FileField(upload_to='sellersaccount/', verbose_name='upload your government id or business license')
    business_name = models.CharField(max_length=1000, null=True, blank=True, verbose_name='company name(optional)')
    phone_number = PhoneNumberField(verbose_name='phonenumber (country code first)')
    country = CountryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name
    
    class Meta():

        verbose_name_plural = 'SellersAccount'

class BuyersAccount(models.Model):
    phone_number = PhoneNumberField(verbose_name='phonenumber (country code first)')
    country = CountryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.country
    
    class Meta():

        verbose_name_plural = 'BuyersAccount'

class Buyers_Sellers(models.Model):
    business_name = models.CharField(max_length=1000, null=True, blank=True, verbose_name='company name(optional)')
    phone_number = PhoneNumberField(verbose_name='phonenumber (country code first)')
    country = CountryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name
    
    class Meta():

        verbose_name_plural = 'BuyersAccount'


class AddCoupon(models.Model):

    name = models.CharField(max_length=500)
    category = models.ForeignKey(Product, on_delete=models.CASCADE)
    active_on = models.DateField()
    expire_on = models.DateField()
    number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta():

        verbose_name_plural = 'AddCoupon'



class Coupon(models.Model):
    coupon = models.CharField(max_length=150)
    upload = models.FileField(upload_to='profile_upload')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.coupon

    class Meta():
        verbose_name_plural = 'Coupon'

class BuyCoupon(models.Model):
    coupon = models.CharField(max_length=150)
    upload = models.FileField(upload_to='profile_upload')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.coupon

    class Meta():
        verbose_name_plural = 'BuyCoupon'

class CartCoupon(models.Model):
    coupon = models.CharField(max_length=150)
    upload = models.FileField(upload_to='profile_upload')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.coupon

    class Meta():
        verbose_name_plural = 'CartCoupon'

class Estimate_Shipping(models.Model):
    country = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    postal = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.country

    class Meta():
        verbose_name_plural = 'Estimate_Shipping'





class Profile(models.Model):
    name = models.CharField(max_length=150)
    upload = models.FileField(upload_to='profile_upload')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Profile'



class NewsLetter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'NewsLetter'


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=700)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'NewsLetter'


class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    first_name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=50, verbose_name='last name')
    phone_number = PhoneNumberField(verbose_name='enter phonenumber(country code first)')
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    apartment = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    country = CountryField(verbose_name='select country')
    post_code = models.IntegerField(verbose_name='zip postal code')
    state = models.CharField(max_length=2000, verbose_name='regional state')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name
    
    
    class Meta():

        verbose_name_plural = 'Checkout'

class Order_Items(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    # def __str__(self):
    #     return self.
    
    
    class Meta():

        verbose_name_plural = 'Order_Items'





class Cart_Shipping(models.Model):
    CHOICES = (
    ('select1', 'international shipping|10-15 15-30 days'),
    ('select2', 'local shipping|1-3 2-5 days '),
    


)


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(Order, on_delete=models.CASCADE)

    select = models.CharField(max_length=1000, choices=CHOICES, verbose_name='select shipping method')

    def __str__(self):
        return self.select
    
    class Meta():

        verbose_name_plural = 'Cart_Shipping'

    

class Order2(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    created_by = models.CharField(max_length=50, verbose_name='last name')
    phone_number = PhoneNumberField(verbose_name='enter phonenumber(country code first)')
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    apartment = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    country = CountryField(verbose_name='select country')
    post_code = models.IntegerField(verbose_name='zip postal code')
    state = models.CharField(max_length=2000, verbose_name='regional state')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name
    
    
    class Meta():
        verbose_name_plural = 'Order2'

class Order2_Items(models.Model):
    order = models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='details', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    # def __str__(self):
    #     return self.
    
    
    class Meta():

        verbose_name_plural = 'Order2_Items'



class Buy_Now_Shipping(models.Model):
    CHOICES = (
    ('select1', 'international shipping|10-15 15-30 days'),
    ('select2', 'local shipping|1-3 2-5 days '),
    

)


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(Order2, on_delete=models.CASCADE)

    select = models.CharField(max_length=1000, choices=CHOICES, verbose_name='select shipping method')

    def __str__(self):
        return self.select
    
    class Meta():

        verbose_name_plural = 'Buy_Now_Shipping'




STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post_Category(models.Model):
    category = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category
    
    class Meta():
        verbose_name_plural = 'Post_Category'



class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    created_by = models.CharField(max_length=100, verbose_name='author')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='blog-video', null=True, blank=True, verbose_name='upload a video(optional)')
    num_site = models.IntegerField(default=0, verbose_name='visited')
    phone_number = PhoneNumberField(verbose_name='enter phonenumber(country code first)')
    category = models.ForeignKey(Post_Category, on_delete=models.CASCADE, verbose_name='select category')
    email = models.EmailField()
    country = CountryField(verbose_name='select country')
    description = models.TextField()
    image = models.FileField(upload_to='blog-image', verbose_name='upload an image')
    thumbnail = models.FileField(upload_to='thumbnail/', null=True, verbose_name='upload a photo')
    multiple = models.FileField(upload_to='multiple/', verbose_name='upload a photo')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='enough_likes', blank=True)
    favourite = models.ManyToManyField(User, related_name='enough_favourite', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()

    
    class Meta():
        verbose_name_plural = 'Post'

    class Meta():

        ordering = ['-created_at',]



class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.FileField(upload_to='BLOG-COMMENT-IMAGE', verbose_name='upload personal image')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title

    class Meta():
        verbose_name_plural = 'Comment'

class Reply(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    image = models.FileField(upload_to='BLOG-COMMENT-IMAGE', verbose_name='upload personal image')
    comment = models.TextField()
    post = models.ForeignKey(Comment, related_name='load', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Reply'



