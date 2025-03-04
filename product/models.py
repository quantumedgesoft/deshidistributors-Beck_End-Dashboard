from django.db import models
from django.utils.text import slugify
from home.extra_module import previous_image_delete_os, image_delete_os

def generate_unique_slug(model_object, slug_field):
    slug = slugify(slug_field)
    unique_slug = slug
    num = 1
    while model_object.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{slug}-{num}'
        num+=1
    return unique_slug


class Tag(models.Model):
    name = models.CharField(max_length=55)
    
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='image/category/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.pk and Category.objects.filter(pk=self.pk).exists():
            old_instance = Category.objects.get(pk=self.pk)
            previous_image_delete_os(old_instance.image, self.image)

        self.slug = generate_unique_slug(Category, self.title)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        image_delete_os(self.image)
        super().delete(*args, **kwargs)
    
    
    def __str__(self):
        return self.title


class Product(models.Model):
    PRODUCT_TYPE = (
        ('Active', 'Active'),
        ('Upcomming', 'Upcomming'),
        ('Deactive', 'Deactive'),
    )
    category = models.ForeignKey(Category, blank=True, null=True, related_name='products', on_delete=models.DO_NOTHING)
    tags = models.ForeignKey(Tag, blank=True, null=True, related_name='products', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='image/product/', blank=True, null=True)
    product_type = models.CharField(max_length=25, choices=PRODUCT_TYPE, default='Active')
    
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.pk and Product.objects.filter(pk=self.pk).exists():
            old_instance = Product.objects.get(pk=self.pk)
            previous_image_delete_os(old_instance.image, self.image)
        self.slug = generate_unique_slug(Product, self.title)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        image_delete_os(self.image)
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.title




