from rest_framework import routers

from .views import PositionViewSet

router = routers.DefaultRouter()
router.register(r'positions', PositionViewSet)
