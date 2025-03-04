from .models import ContentManagementSettings
from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response
from .serializers import *
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.exceptions import TokenError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView

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
    filterset_fields = ['is_active', 'category']
    search_fields = ['name', 'image', 'category__title']
    parser_classes = [MultiPartParser]
    
    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                {
                    'status': True,
                    'message': 'Slider Successfully Updated!',
                    'slider': response.data
                }, status=status.HTTP_200_OK
            )
        except:
            return Response(
                    {
                        'status': False,
                        'message': 'Slider not found!'
                    }, status=status.HTTP_204_NO_CONTENT
                )
    
    def destroy(self, request, *args, **kwargs):
        slider_pk = kwargs.get('pk')
        try:
            if Slider.objects.filter(pk=slider_pk).exists():
                slider = Slider.objects.get(id=slider_pk)
                slider.delete()
                return Response(
                    {
                        'status': True,
                        'message': 'Slider Successfully Deleted!'
                    }, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'status': False,
                        'message': 'Slider not found!'
                    }, status=status.HTTP_204_NO_CONTENT
                )
        except Exception as e:
            return Response(
                {
                    'status': False,
                    'message': 'Somethings wrong!',
                    'error': str(e)
                }, status=status.HTTP_204_NO_CONTENT
            )        
    
    def create(self, request, *args, **kwargs):
        category_id = request.data.get('category')
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
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


class DiscountCardViewSet(viewsets.ModelViewSet):
    queryset = DiscountCard.objects.all()
    serializer_class = DiscountCardSerializer
    permission_classes = [AdminCreationPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = []
    search_fields = ['title', 'offer']
    parser_classes = [MultiPartParser]
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                'status': True,
                'message': 'Discount Card Successfully Created!',
                'discount card': response.data
            }, status=status.HTTP_201_CREATED
        )
    
    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                {
                    'status': True,
                    'message': 'Discount Card Successfully Updated!',
                    'slider': response.data
                }, status=status.HTTP_200_OK
            )
        except:
            return Response(
                    {
                        'status': False,
                        'message': 'Discount Card not found!'
                    }, status=status.HTTP_204_NO_CONTENT
                )
    
    def destroy(self, request, *args, **kwargs):
        discount_card_pk = kwargs.get('pk')
        try:
            if DiscountCard.objects.filter(pk=discount_card_pk).exists():
                discount_card = DiscountCard.objects.get(id=discount_card_pk)
                discount_card.delete()
                return Response(
                    {
                        'status': True,
                        'message': 'Discount Card Successfully Deleted!'
                    }, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'status': False,
                        'message': 'Discount Card not found!'
                    }, status=status.HTTP_204_NO_CONTENT
                )
        except Exception as e:
            return Response(
                {
                    'status': False,
                    'message': 'Somethings wrong!',
                    'error': str(e)
                }, status=status.HTTP_204_NO_CONTENT
            )   

class OurTestimonialViewSet(viewsets.ModelViewSet):
    queryset = OurTestimonial.objects.all()
    serializer_class = OurTestimonialSerializer
    permission_classes = [AdminCreationPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['rating', 'designation', 'is_active']
    search_fields = ['name', 'designation', 'review']
    parser_classes = [MultiPartParser]
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                'status': True,
                'message': 'Testimonial Successfully Created!',
                'discount card': response.data
            }, status=status.HTTP_201_CREATED
        )
    
    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                {
                    'status': True,
                    'message': 'Testimonial Successfully Updated!',
                    'slider': response.data
                }, status=status.HTTP_200_OK
            )
        except:
            return Response(
                    {
                        'status': False,
                        'message': 'Testimonial not found!'
                    }, status=status.HTTP_204_NO_CONTENT
                )
    
    def destroy(self, request, *args, **kwargs):
        testimonial_pk = kwargs.get('pk')
        try:
            if OurTestimonial.objects.filter(pk=testimonial_pk).exists():
                testimonial = OurTestimonial.objects.get(id=testimonial_pk)
                testimonial.delete()
                return Response(
                    {
                        'status': True,
                        'message': 'Testimonial Successfully Deleted!'
                    }, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'status': False,
                        'message': 'Testimonial not found!'
                    }, status=status.HTTP_204_NO_CONTENT
                )
        except Exception as e:
            return Response(
                {
                    'status': False,
                    'message': 'Somethings wrong!',
                    'error': str(e)
                }, status=status.HTTP_204_NO_CONTENT
            )


class ContentManagementSettingsView(RetrieveAPIView):
    queryset = ContentManagementSettings.objects.all()
    serializer_class = ContentManagementSettingsSerializer
    
    def get(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        if instance is None:
            return Response({"status": False, "message": "No content found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response({"status": True, "data": serializer.data}, status=status.HTTP_200_OK)
    
    # def get_queryset(self):
    #     return ContentManagementSettings.objects.all().first()
    
    # def get_object(self):
    #     return self.queryset.first()

# class ContentManagementSettingsViewSets(viewsets.ModelViewSet):
#     queryset = ContentManagementSettings.objects.all()
#     serializer_class = ContentManagementSettingsSerializer
#     permission_classes = [AdminCreationPermission]
#     parser_classes = [MultiPartParser]
    
#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         return Response(
#             {
#                 'status': True,
#                 'message': 'Content Successfully Created!',
#                 'content': response.data
#             }, status=status.HTTP_201_CREATED
#         )
    
#     def update(self, request, *args, **kwargs):
#         query = self.get_object()
#         print(query)
#         try:
#             response = super().update(request, *args, **kwargs)
#             return Response(
#                 {
#                     'status': True,
#                     'message': 'Content Successfully Updated!',
#                     'slider': response.data
#                 }, status=status.HTTP_200_OK
#             )
#         except Exception as e:
#             return Response(
#                     {
#                         'status': False,
#                         'message': 'Content not found!',
#                         'error': str(e)
#                     }, status=status.HTTP_204_NO_CONTENT
#                 )
    
#     def destroy(self, request, *args, **kwargs):
#         content_pk = kwargs.get('pk')
#         try:
#             if ContentManagementSettings.objects.filter(pk=content_pk).exists():
#                 content = ContentManagementSettings.objects.get(id=content_pk)
#                 content.delete()
#                 return Response(
#                     {
#                         'status': True,
#                         'message': 'Content Successfully Deleted!'
#                     }, status=status.HTTP_200_OK
#                 )
#             else:
#                 return Response(
#                     {
#                         'status': False,
#                         'message': 'Content not found!'
#                     }, status=status.HTTP_204_NO_CONTENT
#                 )
#         except Exception as e:
#             return Response(
#                 {
#                     'status': False,
#                     'message': 'Somethings wrong!',
#                     'error': str(e)
#                 }, status=status.HTTP_204_NO_CONTENT
#             )   



class OurPartnerViewSet(viewsets.ModelViewSet):
    queryset = OurPartner.objects.all()
    serializer_class = OurPartnerSerializer
    permission_classes = [AdminCreationPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    parser_classes = [MultiPartParser]
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                'status': True,
                'message': 'Partner Successfully Created!',
                'discount card': response.data
            }, status=status.HTTP_201_CREATED
        )
    
    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                {
                    'status': True,
                    'message': 'Partner Successfully Updated!',
                    'slider': response.data
                }, status=status.HTTP_200_OK
            )
        except:
            return Response(
                    {
                        'status': False,
                        'message': 'Partner not found!'
                    }, status=status.HTTP_204_NO_CONTENT
                )
    
    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        try:
            if OurPartner.objects.filter(id=id).exists():
                our_partner = OurPartner.objects.get(id=id)
                our_partner.delete()
                return Response(
                    {
                        'status': True,
                        'message': 'Partner Successfully Deleted!'
                    }, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'status': False,
                        'message': 'Partner not found!'
                    }, status=status.HTTP_204_NO_CONTENT
                )
        except Exception as e:
            return Response(
                {
                    'status': False,
                    'message': 'Somethings wrong!',
                    'error': str(e)
                }, status=status.HTTP_204_NO_CONTENT
            )


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'phone', 'message']
    
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(
            {
                'status': True,
                'message': 'Thanks for contacting with us!'
            }, status=status.HTTP_201_CREATED
        )


class OurTeamViewSet(viewsets.ModelViewSet):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer
    permission_classes = [AdminCreationPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['designation']
    search_fields = ['name', 'phone', 'email', 'designation', 'message']
    parser_classes = [MultiPartParser]
    


