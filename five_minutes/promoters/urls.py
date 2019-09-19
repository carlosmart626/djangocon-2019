"""
URLs necessary for the Promoters Application
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from promoters import views

# Create a router and register our viewsets with it.
ROUTER = DefaultRouter(trailing_slash=False)
ROUTER.register(r'promoters', views.PromoterViewSet)
ROUTER.register(r'promoter-spaces', views.PromoterSpaceViewSet)

urlpatterns = [
    url(r'^', include(ROUTER.urls)),
]
