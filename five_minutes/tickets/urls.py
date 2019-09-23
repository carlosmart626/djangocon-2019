"""
URLs necessary for the Tickets Application
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from tickets import views

# Create a router and register our viewsets with it.
ROUTER = DefaultRouter(trailing_slash=False)
ROUTER.register(r'tickets', views.TicketViewSet)
ROUTER.register(r'use-ticket', views.UserTicketViewSet)

urlpatterns = [
    url(r'^', include(ROUTER.urls)),
    url(r'my-tickets', views.MyTicketsView.as_view(), name='my-tickets'),
]
