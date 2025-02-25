from django.db import models
from django.utils.text import slugify

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
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image/category/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.slug = generate_unique_slug(Category, self.slug)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Product(models.Model):
    PRODUCT_TYPE = (
        ('Active', 'Active'),
        ('Upcomming', 'Upcomming'),
        ('Deactive', 'Deactive'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    short_description = models.TextField()
    details = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='image/product/', blank=True, null=True)
    product_type = models.CharField(max_length=25, choices=PRODUCT_TYPE, default='Active')
    
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.slug = generate_unique_slug(Category, self.slug)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


    

