from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import *


# ViewSets
# class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = [permissions.IsAuthenticated]

class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    # permission_classes = [IsAdminOrReadOnly]

class HeroSectionViewSet(viewsets.ModelViewSet):
    queryset = Hero_Section.objects.all()
    serializer_class = HeroSectionSerializer
    # permission_classes = [IsAdminOrReadOnly]

class DiscountCardViewSet(viewsets.ModelViewSet):
    queryset = DiscountCard.objects.all()
    serializer_class = DiscountCardSerializer
    # permission_classes = [IsAdminOrReadOnly]

class SiteQualityCardViewSet(viewsets.ModelViewSet):
    queryset = SiteQualityCard.objects.all()
    serializer_class = SiteQualityCardSerializer
    # permission_classes = [IsAdminOrReadOnly]

class OurTestimonialViewSet(viewsets.ModelViewSet):
    queryset = OurTestimonial.objects.all()
    serializer_class = OurTestimonialSerializer
    # permission_classes = [IsAdminOrReadOnly]

class ContentManagementSettingsViewSet(viewsets.ModelViewSet):
    queryset = ContentManagementSettings.objects.all()
    serializer_class = ContentManagementSettingsSerializer
    # permission_classes = [IsAdminOrReadOnly]

