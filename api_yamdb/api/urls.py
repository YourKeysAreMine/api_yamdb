from django.urls import include, path
from api.views import GenreViewSet, CategoryViewSet
from rest_framework import routers


v1_router = routers.DefaultRouter()
v1_router.register(r'genres', GenreViewSet, basename='genres')
v1_router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
