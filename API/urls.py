from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from . import views

# Роутеры ВьюСетов
router = routers.DefaultRouter()
router.register(r"users", views.UsersViewset)
router.register(r"coords", views.CoordsViewset)
router.register(r"level", views.LevelViewset)
router.register(r"images", views.ImagesViewset)
router.register(r"submitData", views.PerevalsViewset, basename="submitdata")


urlpatterns = [
    path("", include(router.urls)),
]
