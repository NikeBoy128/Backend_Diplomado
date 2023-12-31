from django import views
from rest_framework import routers
from projects.views import WhoAmIView
from .api import projectViewSet
from .views import AutosViewSet, GroupViewSet,ViajesViewSet,GastosViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
   openapi.Info(
      title="Your Project API",
      default_version='v1',
      description="API documentation for Your Project",
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('usuarios', projectViewSet, 'projects')
router.register('autos',AutosViewSet, 'autos')
router.register('grupos',GroupViewSet, 'grupos')
router.register('viajes',ViajesViewSet, 'viajes')
router.register('gastos',GastosViewSet, 'gastos')
urlpatterns = [
    
    path('usuario_autenticado/', WhoAmIView.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls 