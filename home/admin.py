from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Slider)
admin.site.register(DiscountCard)
admin.site.register(OurTestimonial)
admin.site.register(ContentManagementSettings)