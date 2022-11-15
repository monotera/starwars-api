from characters.views import CharacterViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CharacterViewSet, basename='')
urlpatterns = router.urls