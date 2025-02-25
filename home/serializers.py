from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'user_type', 'created_at')

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