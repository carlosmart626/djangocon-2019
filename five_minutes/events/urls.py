"""
URLs necessary for the Events Application
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from events import views

# Create a router and register our viewsets with it.
ROUTER = DefaultRouter(trailing_slash=False)
ROUTER.register(r'events', views.EventViewSet)

urlpatterns = [
    url(r'^', include(ROUTER.urls)),
]
