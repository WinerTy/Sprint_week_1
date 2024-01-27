from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from . import views

# Роутеры ВьюСетов
router = routers.DefaultRouter()
router.register(r'users', views.UsersViewset)
router.register(r'coords', views.CoordsViewset)
router.register(r'level', views.LevelViewset)
router.register(r'images', views.ImagesViewset)
router.register(r'submitData', views.PerevalsViewset, basename='submitdata')


schema_view = get_schema_view(
   openapi.Info(
      title="Документация для REST API(DRF)",
      default_version='v1.0.0',
      description="Инструкция пользовнаия API",
   ),
   public=True,
)


urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
