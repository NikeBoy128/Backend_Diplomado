from rest_framework import routers
from .api import projectViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path

schema_view = get_schema_view(
   openapi.Info(
      title="Your Project API",
      default_version='v1',
      description="API documentation for Your Project",
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('api/projects', projectViewSet, 'projects')

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + router.urls