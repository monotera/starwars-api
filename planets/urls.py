from .views import PlanetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PlanetViewSet, basename='')
urlpatterns = router.urls