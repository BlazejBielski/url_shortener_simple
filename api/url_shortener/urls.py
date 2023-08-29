from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import viewsets

app_name = 'url_shortener'

router = DefaultRouter()
router.register(r'urls', viewsets.URLViewSet, basename="url")


urlpatterns = [
    path('', include(router.urls)),
]
