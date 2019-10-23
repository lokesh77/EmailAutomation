from django.conf.urls import url, include
from django.urls import path
from . import views
from .apiviews import CustomerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customer', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name='index'),
]