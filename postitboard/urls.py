from rest_framework.routers import DefaultRouter

from .api import GroupViewSet, MessageViewSet

router = DefaultRouter()

router.register(r'groups', GroupViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = router.urls
