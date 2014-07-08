from rest_framework import routers

from .views import AssetViewSet


router = routers.DefaultRouter()
router.register(r'assets', AssetViewSet)
