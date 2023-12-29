from django.contrib import admin
from django.urls import path

from asosiy.views import *



from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('suvlar/', SuvlarAPI.as_view()),
    path('suv/int:<pk>/', SuvAPI.as_view()),
    path('mijozlar/', MijozlarAPI.as_view()),
    path('mijoz/int:<pk>/', MijozAPI.as_view()),
    path('buyurtmalar/', BuyurtmalarAPI.as_view()),
    path('haydovchilar/', HaydovchilarAPI.as_view()),
    path('adminlar/', AdminlarAPI.as_view()),
    path('haydovchi/int:<pk>/', HaydovchiAPI.as_view()),
    path('admin/int:<pk>/', AdminAPI.as_view()),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
