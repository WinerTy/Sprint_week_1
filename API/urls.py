from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UsersViewset)
router.register(r'coords', views.CoordsViewset)
router.register(r'level', views.LevelViewset)
router.register(r'images', views.ImagesViewset)
router.register(r'submitData', views.PerevalsViewset)


urlpatterns = [
    path('', include(router.urls)),
]