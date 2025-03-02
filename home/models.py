from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import Category
from django.core.files.storage import default_storage

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
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='image/slider/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='slider')
    is_active = models.BooleanField(default=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Slider.objects.get(pk=self.pk)
            if old_instance and old_instance.image and old_instance.image != self.image:
                if default_storage.exists(old_instance.image.name):
                    default_storage.delete(old_instance.image.name)
        
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.image and default_storage.exists(self.image.name):
            default_storage.delete(self.image.name)
        return super().delete( *args, **kwargs)
    
    def __str__(self):
        return self.category.title



class DiscountCard(models.Model):
    image = models.ImageField(upload_to='image/discount-card/', blank=True, null=True)
    title = models.CharField(max_length=100)
    offer = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = DiscountCard.objects.get(pk=self.pk)
            if old_instance and old_instance.image and old_instance.image != self.image:
                if default_storage.exists(old_instance.image.name):
                    default_storage.delete(old_instance.image.name)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.image and default_storage.exists(self.image.name):
            default_storage.delete(self.image.name)
        return super().delete( *args, **kwargs)
    
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
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = OurTestimonial.objects.get(pk=self.pk)
            if old_instance and old_instance.picture and old_instance.picture != self.picture:
                if default_storage.exists(old_instance.picture.name):
                    default_storage.delete(old_instance.picture.name)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.picture and default_storage.exists(self.picture.name):
            default_storage.delete(self.picture.name)
        return super().delete( *args, **kwargs)
    
    def __str__(self):
        return self.name


class ContentManagementSettings(models.Model):
    main_logo = models.ImageField(upload_to='image/logo/', blank=True, null=True)
    fav_icon = models.ImageField(upload_to='image/logo/', blank=True, null=True)
    secondary_logo = models.ImageField(upload_to='image/logo/', blank=True, null=True)
    
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_slogan = models.CharField(max_length=200, blank=True, null=True)
    company_details = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    wokring_day_from = models.CharField(max_length=20, blank=True, null=True)
    wokring_day_to = models.CharField(max_length=20, blank=True, null=True)
    wokring_hour_from = models.CharField(max_length=20, blank=True, null=True)
    wokring_hour_to = models.CharField(max_length=20, blank=True, null=True)
    copyright_year = models.CharField(max_length=4, blank=True, null=True)
    
    hero_h4_title = models.CharField(max_length=100)
    hero_h1_title = models.CharField(max_length=100)
    
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
    
    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = ContentManagementSettings.objects.get(pk=self.pk)
            if old_instance:
                #for main logo
                if old_instance.main_logo and old_instance.main_logo != self.main_logo:
                    if default_storage.exists(old_instance.main_logo.name):
                        default_storage.delete(old_instance.main_logo.name)
                
                #for fav icon
                if old_instance.fav_icon and old_instance.fav_icon != self.fav_icon:
                    if default_storage.exists(old_instance.fav_icon.name):
                        default_storage.delete(old_instance.fav_icon.name)
                
                #for secondary logo
                if old_instance.secondary_logo and old_instance.secondary_logo != self.secondary_logo:
                    if default_storage.exists(old_instance.secondary_logo.name):
                        default_storage.delete(old_instance.secondary_logo.name)
            
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        #for main logo
        if self.main_logo and default_storage.exists(self.main_logo.name):
            default_storage.delete(self.main_logo.name)
        
        #for fav icon
        if self.fav_icon and default_storage.exists(self.fav_icon.name):
            default_storage.delete(self.fav_icon.name)
        
        #for secondary logo
        if self.secondary_logo and default_storage.exists(self.secondary_logo.name):
            default_storage.delete(self.secondary_logo.name)
        
        return super().delete( *args, **kwargs)
    
    
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







