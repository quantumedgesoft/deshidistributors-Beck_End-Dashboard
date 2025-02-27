from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from product.serializers import CategorySerializer
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'email', 'username', 'user_type', 'password')






class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero_Section
        fields = '__all__'

class DiscountCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCard
        fields = '__all__'

class SiteQualityCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteQualityCard
        fields = '__all__'

class OurTestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTestimonial
        fields = '__all__'

class ContentManagementSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentManagementSettings
        fields = '__all__'