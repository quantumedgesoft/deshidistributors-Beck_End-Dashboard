from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import *
from product.models import Category

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'email', 'username', 'user_type', 'password')





class SliderSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Slider
        fields = '__all__'
    
    def get_category(self, obj):
        request = self.context.get('request')
        return {
            "id": obj.category.id,
            "title": obj.category.title,
            "slug": obj.category.slug,
            "image": request.build_absolute_uri(obj.category.image.url) if obj.category.image else None,
            "is_active": obj.category.is_active,
        } if obj.category else None
    
    def create(self, validated_data):
        request = self.context.get('request')
        category_id = request.data.get('category')
        if not category_id:
            raise serializers.ValidationError({"category": "This field is required!"})
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise serializers.ValidationError({"category": "Invalid category ID."})
        validated_data['category'] = category
        return super().create(validated_data)

class CardSection01Serializer(serializers.ModelSerializer):
    class Meta:
        model = CardSection01
        fields = '__all__'

class DiscountCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCard
        fields = '__all__'

class OurTestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTestimonial
        fields = '__all__'

class ContentManagementSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentManagementSettings
        fields = '__all__'


class OurPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurPartner
        fields = '__all__'



class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'
