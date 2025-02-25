from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import Category

class CustomUser(AbstractUser):
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Super Admin', 'Super Admin'),
        ('Customer', 'Customer'),
        ('Staff', 'Staff'),
    )
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if self.user_type == 'Admin' or self.user_type == 'Super Admin':
            self.is_superuser = True
            self.is_staff = True
        if self.user_type == 'Staff':
            self.is_staff = True
        if self.user_type == 'Customer':
            self.is_superuser = False
            self.is_staff = False
        super().save(*args, **kwargs)




class Slider(models.Model):
    image = models.ImageField(upload_to='image/slider/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='slider')
    is_active = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category.title


class Hero_Section(models.Model):
    h4_title = models.CharField(max_length=100)
    h1_title = models.CharField(max_length=100)
    slider = models.ManyToManyField(Slider)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Hero Section - {self.id}'


class DiscountCard(models.Model):
    image = models.ImageField(upload_to='image/discount-card/', blank=True, null=True)
    title = models.CharField(max_length=100)
    offer = models.CharField(max_length=100)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class SiteQualityCard(models.Model):
    title = models.CharField(max_length=55)
    count = models.PositiveIntegerField()
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class OurTestimonial(models.Model):
    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    picture = models.ImageField(upload_to='image/our-testimonial/', blank=True, null=True)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    rating = models.CharField(max_length=1, choices=RATING, blank=True)
    review = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name




class ContentManagementSettings(models.Model):
    main_logo = models.ImageField(upload_to='image/logo/', blank=True, null=True)
    fav_icon = models.ImageField(upload_to='image/logo/', blank=True, null=True)
    main_logo = models.ImageField(upload_to='image/logo/', blank=True, null=True)
    
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_slogan = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    wokring_day_from = models.CharField(max_length=20, blank=True, null=True)
    wokring_day_to = models.CharField(max_length=20, blank=True, null=True)
    wokring_hour_from = models.CharField(max_length=20, blank=True, null=True)
    wokring_hour_to = models.CharField(max_length=20, blank=True, null=True)
    copyright_year = models.CharField(max_length=4, blank=True, null=True)
    
    satisfied_customer_count = models.PositiveIntegerField(blank=True, null=True)
    quality_service_count = models.PositiveIntegerField(blank=True, null=True)
    quality_certificate_count = models.PositiveIntegerField(blank=True, null=True)
    available_product_count = models.PositiveIntegerField(blank=True, null=True)
    
    product_section_title_1 = models.CharField(max_length=200, blank=True, null=True)
    product_section_description_1 = models.TextField(blank=True, null=True)
    product_section_title_2 = models.CharField(max_length=200, blank=True, null=True)
    product_section_description_2 = models.TextField(blank=True, null=True)
    product_section_title_3 = models.CharField(max_length=200, blank=True, null=True)
    product_section_description_3 = models.TextField(blank=True, null=True)
    
    testimonial_title = models.CharField(max_length=200, blank=True, null=True)
    testimonial_description = models.TextField(blank=True, null=True)
    
    
    facebook = models.URLField(max_length=250, blank=True, null=True)
    linkedin = models.URLField(max_length=250, blank=True, null=True)
    twitter = models.URLField(max_length=250, blank=True, null=True)
    youtube = models.URLField(max_length=250, blank=True, null=True)
    
    
    # is_hero = models.BooleanField(default=True)
    # is_service = models.BooleanField(default=True)
    # is_about = models.BooleanField(default=True)
    # is_portfolio = models.BooleanField(default=True)
    # is_video  = models.BooleanField(default=True)
    # is_work_process = models.BooleanField(default=True)
    # is_team = models.BooleanField(default=True)
    # is_faq = models.BooleanField(default=True)
    # is_testmonial = models.BooleanField(default=True)
    # is_cta = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.company_name} | {self.id}'







