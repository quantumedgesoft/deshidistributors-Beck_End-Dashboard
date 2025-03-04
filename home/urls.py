from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'sliders', SliderViewSet)
router.register(r'discount-cards', DiscountCardViewSet)
router.register(r'our-testimonials', OurTestimonialViewSet)
router.register(r'our-partner', OurPartnerViewSet)
router.register(r'contact-us', ContactUsViewSet)
router.register(r'team', OurTeamViewSet)
router.register(r'content-management-settings', ContentManagementSettingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    path('login/', TokenObtainPairView.as_view(), name='admin-login'),
    path('user-create/', CustomUserViewSet.as_view(), name='user-create'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token-verify/', AuthTokenVerifyViews.as_view(), name='token-verify'),
]