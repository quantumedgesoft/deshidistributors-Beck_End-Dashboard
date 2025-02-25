from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView
from django.urls import path, include
from .views import *

router = DefaultRouter()
# router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'sliders', SliderViewSet)
router.register(r'hero-sections', HeroSectionViewSet)
router.register(r'discount-cards', DiscountCardViewSet)
router.register(r'site-quality-cards', SiteQualityCardViewSet)
router.register(r'our-testimonials', OurTestimonialViewSet)
router.register(r'content-management-settings', ContentManagementSettingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    path('login/', TokenObtainPairView.as_view(), name='admin-login'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token-verify'),
]