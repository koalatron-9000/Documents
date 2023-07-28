from django.contrib import admin
from django.urls import include, path
from .views import HomePageView, UserViewSet, GroupViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    #path('a/', include('rest_framework.urls', namespace= 'rest_framework')),
    path('api-auth/', include('rest_framework.urls')),
]
