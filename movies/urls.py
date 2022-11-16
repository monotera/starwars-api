from movies.views import MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', MovieViewSet, basename='')
urlpatterns = router.urls