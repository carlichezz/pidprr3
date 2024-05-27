from rest_framework import routers
from .api import StudentViewSet, FacultadViewSet, GrupoViewSet
from .views import CustomAuthTokenView

router = routers.DefaultRouter()
router.register('api/students', StudentViewSet, 'students')
router.register('api/facultad', FacultadViewSet, 'facultades')
router.register('api/grupo', GrupoViewSet, 'grupos')
router.register(r'auth', CustomAuthTokenView, basename='auth') 

urlpatterns = router.urls