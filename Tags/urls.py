"""djangorest_demo URL Configuration"""
from django.urls import path
from rest_framework import routers

from .views import TagsViewSet, UsersViewSet

router = routers.DefaultRouter()
router.register('', UsersViewSet)
# router.register('', TagsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
