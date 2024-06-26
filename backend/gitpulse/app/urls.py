# app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RepositoryViewSet, index

router = DefaultRouter()
router.register(r'repositories', RepositoryViewSet)

urlpatterns = [
    path('',index),
    path('', include(router.urls)),
]
