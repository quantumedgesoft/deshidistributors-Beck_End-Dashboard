from django.db import models
from django.utils.text import slugify
from django.core.files.storage import default_storage

def generate_unique_slug(model_object, slug_field):
    slug = slugify(slug_field)
    unique_slug = slug
    num = 1
    while model_object.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{slug}-{num}'
        num+=1
    return unique_slug

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='image/category/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Category.objects.get(pk=self.pk)
            if old_instance and old_instance.image and old_instance.image != self.image:
                if default_storage.exists(old_instance.image.name):
                    default_storage.delete(old_instance.image.name)
        
        self.slug = generate_unique_slug(Category, self.title)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.image and default_storage.exists(self.image.name):
            default_storage.delete(self.image.name)
        super().delete(*args, **kwargs)
    
    
    def __str__(self):
        return self.title


class Product(models.Model):
    PRODUCT_TYPE = (
        ('Active', 'Active'),
        ('Upcomming', 'Upcomming'),
        ('Deactive', 'Deactive'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='image/product/', blank=True, null=True)
    product_type = models.CharField(max_length=25, choices=PRODUCT_TYPE, default='Active')
    
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Product.objects.get(pk=self.pk)
            if old_instance and old_instance.image and old_instance.image != self.image:
                if default_storage.exists(old_instance.image.name):
                    default_storage.delete(old_instance.image.name)
        
        self.slug = generate_unique_slug(Product, self.slug)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.image and default_storage.exists(self.image.name):
            default_storage.delete(self.image.name)
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.title




