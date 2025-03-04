from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import Category
from .extra_module import *

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
        if self.pk and Slider.objects.filter(pk=self.pk).exists():
            old_instance = Slider.objects.get(pk=self.pk)
            previous_image_delete_os(old_instance.image, self.image)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        image_delete_os(self.image)
        return super().delete( *args, **kwargs)
    
    def __str__(self):
        return self.category.title



class DiscountCard(models.Model):
    image = models.ImageField(upload_to='image/discount-card/', blank=True, null=True)
    title = models.CharField(max_length=100)
    offer = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        if self.pk and DiscountCard.objects.filter(pk=self.pk).exists():
            old_instance = DiscountCard.objects.get(pk=self.pk)
            previous_image_delete_os(old_instance.image, self.image)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        image_delete_os(self.image)
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
        if self.pk and OurTestimonial.objects.filter(pk=self.pk).exists():
            old_instance = OurTestimonial.objects.get(pk=self.pk)
            previous_image_delete_os(old_instance.picture, self.picture)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        image_delete_os(self.picture)
        return super().delete( *args, **kwargs)
    
    def __str__(self):
        return self.name


class ContentManagementSettings(models.Model):
    main_logo = models.ImageField(upload_to='image/logo/', blank=True, null=True)
    fav_icon = models.ImageField(upload_to='image/logo/', blank=True, null=True)
    secondary_logo = models.ImageField(upload_to='image/logo/', blank=True, null=True)
    video_content = models.FileField(upload_to='video/home-content/', blank=True, null=True)
    
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_slogan = models.CharField(max_length=200, blank=True, null=True)
    company_details = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    whatspp_number = models.CharField(max_length=20, blank=True, null=True)
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
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def save(self, *args, **kwargs):
        if self.pk and ContentManagementSettings.objects.filter(pk=self.pk).exists():
            old_instance = ContentManagementSettings.objects.get(pk=self.pk)
            previous_image_delete_os(old_instance.main_logo, self.main_logo)
            previous_image_delete_os(old_instance.fav_icon, self.fav_icon)
            previous_image_delete_os(old_instance.secondary_logo, self.secondary_logo)
            previous_image_delete_os(old_instance.video_content, self.video_content)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        image_delete_os(self.main_logo)
        image_delete_os(self.fav_icon)
        image_delete_os(self.secondary_logo)
        image_delete_os(self.video_content)
        return super().delete( *args, **kwargs)
    
    def __str__(self):
        return f'{self.company_name} | {self.id}'



class OurPartner(models.Model):
    company = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='image/partner-logo/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.pk and OurPartner.objects.filter(pk=self.pk).exists():
            old_instance = OurPartner.objects.get(pk=self.pk)
            previous_image_delete_os(old_instance.logo, self.logo)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        image_delete_os(self.logo)
        return super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.company
    


class ContactUs(models.Model):
    name = models.CharField(max_length=55)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    message = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} | {self.email}"


class OurTeam(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=155, blank=True, null=True)
    designation = models.CharField(max_length=55)
    message = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='image/team/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.pk and OurTestimonial.objects.filter(pk=self.pk).exists():
            old_instance = OurTestimonial.objects.get(pk=self.pk)
            previous_image_delete_os(old_instance.picture, self.picture)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        image_delete_os(self.picture)
        return super().delete( *args, **kwargs)
    
    def __str__(self):
        return self.name

