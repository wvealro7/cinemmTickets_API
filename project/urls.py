
from django.contrib import admin
from django.urls import path,include
from tickets import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', views.MoveViewsetAPIView, basename='movie')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('guests/',views.list_create_api_view,name='list-create-guest'),
    path('api/',include(router.urls)),
]
