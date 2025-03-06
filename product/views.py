from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser
from rest_framework.pagination import PageNumberPagination

class CustomPagenumberpagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    def get_paginated_response(self, data):
        request = self.request
        all_items = request.query_params.get('all', 'false').lower() == 'true'
        page_size = request.query_params.get(self.page_size_query_param)
        if all_items or (page_size and page_size.isdigit() and int(page_size) == 0):
            return Response(
                {
                    'count': len(data),
                    'results': data
                }, status=status.HTTP_200_OK
            )
        return super().get_paginated_response(data)
    

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
    pagination_class = CustomPagenumberpagination
    
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
    pagination_class = CustomPagenumberpagination
    
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


class AvailableStoreViewSet(viewsets.ModelViewSet):
    queryset = AvailableStore.objects.all()
    serializer_class = AvailableStoreSerializer
    permission_classes = [AdminCreationPermision]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'link', 'logo']
    parser_classes = [MultiPartParser]
    pagination_class = None
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                'status': True,
                'message': 'Store Successfully Created!',
                'product': response.data
            }, status=status.HTTP_201_CREATED
        )
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {
                'status': True,
                'message': 'Store Successfully Updated!',
                'product': response.data
            }, status=status.HTTP_200_OK
        )
    
    def destroy(self, request, *args, **kwargs):
        store = self.get_object()
        store.delete()
        return Response(
            {
                'status': True,
                'message': 'Store Successfully Deleted!',
            }, status=status.HTTP_204_NO_CONTENT
        )



