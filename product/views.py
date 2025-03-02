from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser

class AdminCreationPermision(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.user_type in {'Admin', 'Super Admin', 'Staff'}


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminCreationPermision]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'is_active']
    search_fields = ['title', 'description', 'slug']
    parser_classes = [MultiPartParser]
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                'status': True, 
                'message': 'Category Successfully Created!',
                'category': response.data,
            }, status=status.HTTP_201_CREATED
        )
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {
                'status': True,
                'message': 'Category Successfully Updated!',
                'category': response.data
            }, status=status.HTTP_200_OK
        )
    
    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        category.delete()
        return Response(
            {
                'status': True,
                'message': 'Category Successfully Deleted!',
            }, status=status.HTTP_204_NO_CONTENT
        )



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AdminCreationPermision]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['product_type']
    search_fields = ['title', 'short_description', 'slug', 'details']
    parser_classes = [MultiPartParser]
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                'status': True,
                'message': 'Product Successfully Created!',
                'product': response.data
            }, status=status.HTTP_201_CREATED
        )
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {
                'status': True,
                'message': 'Product Successfully Updated!',
                'product': response.data
            }, status=status.HTTP_200_OK
        )
    
    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        return Response(
            {
                'status': True,
                'message': 'Product Successfully Deleted!',
            }, status=status.HTTP_204_NO_CONTENT
        )

