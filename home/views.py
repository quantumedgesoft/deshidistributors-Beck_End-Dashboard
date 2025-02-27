from django.shortcuts import render
from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response
from .serializers import *
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.exceptions import TokenError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser

class AdminCreationPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.user_type in {'Admin', 'Super Admin', 'Staff'}

# ViewSets
class CustomUserViewSet(CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AdminCreationPermission]
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {
                    'status': True,
                    'message': 'User Successfully Created!',
                    'user': response.data
                },status=status.HTTP_201_CREATED, headers=headers
            )
        except Exception as e:
            error_dict = serializer.errors
            error_json = {kay: str(value[0]) for kay, value in error_dict.items()}
            return Response(
                {
                    'status': False,
                    'message': 'User creation failed!',
                    'error': error_json
                }, status=status.HTTP_400_BAD_REQUEST
            )

class AuthTokenVerifyViews(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(
                {
                    'status': True,
                    'message': 'Token Verified',
                }, status=status.HTTP_200_OK
            )
        except TokenError as e:
            return Response(
                {
                    'status': False,
                    'message': 'Token is invalid or expired',
                }, status=status.HTTP_401_UNAUTHORIZED
            )




class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = [AdminCreationPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['image', 'category__title']
    parser_classes = [MultiPartParser]
    
    def create(self, request, *args, **kwargs):
        category_id = request.data.get('category')
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
                request.data['category'] = category.id
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(
                    {
                        'status': True,
                        'message': 'Created!',
                        'slider': serializer.data
                    }, status=status.HTTP_201_CREATED
                )
            except Category.DoesNotExist as e:
                return Response(
                    {
                        'status': True,
                        'message': 'Category Does not exist!',
                        'error': str(e)
                    }, status=status.HTTP_400_BAD_REQUEST
                )
    
    
    

class HeroSectionViewSet(viewsets.ModelViewSet):
    queryset = Hero_Section.objects.all()
    serializer_class = HeroSectionSerializer
    permission_classes = [AdminCreationPermission]

class DiscountCardViewSet(viewsets.ModelViewSet):
    queryset = DiscountCard.objects.all()
    serializer_class = DiscountCardSerializer
    permission_classes = [AdminCreationPermission]

class SiteQualityCardViewSet(viewsets.ModelViewSet):
    queryset = SiteQualityCard.objects.all()
    serializer_class = SiteQualityCardSerializer
    permission_classes = [AdminCreationPermission]

class OurTestimonialViewSet(viewsets.ModelViewSet):
    queryset = OurTestimonial.objects.all()
    serializer_class = OurTestimonialSerializer
    permission_classes = [AdminCreationPermission]

class ContentManagementSettingsViewSet(viewsets.ModelViewSet):
    queryset = ContentManagementSettings.objects.all()
    serializer_class = ContentManagementSettingsSerializer
    permission_classes = [AdminCreationPermission]

