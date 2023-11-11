from django import views
from rest_framework import routers
from projects.views import WhoAmIView
from .api import projectViewSet
from .views import AutosViewSet, GroupViewSet,ViajesViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

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
urlpatterns = [
    
    path('usuario_autenticado/', WhoAmIView.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + router.urls