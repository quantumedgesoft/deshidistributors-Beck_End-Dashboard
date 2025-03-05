from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    class Meta:
        model = Product
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
    
    def get_tags(self, obj):
        return {
            "id": obj.tags.id,
            "title": obj.tags.name,
        } if obj.tags else None
    
    def create(self, validated_data):
        request = self.context.get('request')
        category_id = request.data.get('category')
        tag_id = request.data.get('tags')
        if not category_id:
            raise serializers.ValidationError({"category": "This field is required!"})
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise serializers.ValidationError({"category": "Invalid category ID."})
        validated_data['category'] = category
        
        try:
            tags = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            raise serializers.ValidationError({"tags": "Invalid tag ID"})
        validated_data['tags'] = tags
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        request = self.context.get('request')
        category_id = request.data.get('category')
        tag_id = request.data.get('tags')
        
        if category_id:
            category = Category.objects.get(id=category_id)
            validated_data['category'] = category
        if tag_id:
            tags = Tag.objects.get(id=tag_id)
            validated_data['tags'] = tags
        return super().update(instance, validated_data)


class AvailableStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableStore
        fields = '__all__'
