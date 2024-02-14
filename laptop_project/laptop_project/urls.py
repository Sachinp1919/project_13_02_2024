from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from laptop_app.views import LaptopViewSet

router = DefaultRouter()
router.register('laptop', LaptopViewSet, basename='laptop')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls))
]
