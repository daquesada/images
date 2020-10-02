from django.urls import path,include
from .views import ImageViewSet
from rest_framework import routers

app_name = 'api-view'

routers = routers.DefaultRouter()

routers.register('images', ImageViewSet) 

urlpatterns = [
    path('', include(routers.urls), name='view-images')
]