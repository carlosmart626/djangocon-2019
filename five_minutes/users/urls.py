"""
URLs necessary for the Users Application
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from users import views

# Create a router and register our viewsets with it.
ROUTER = DefaultRouter(trailing_slash=False)
ROUTER.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(ROUTER.urls)),
]