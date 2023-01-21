from django.urls import include, path
from api.views import GenreViewSet, CategoryViewSet, RegistrationView
from rest_framework import routers


v1_router = routers.DefaultRouter()
v1_router.register(r'genres', GenreViewSet, basename='genres')
v1_router.register(r'categories', CategoryViewSet, basename='categories')
v1_router.register(r'auth/signup', RegistrationView, basename='signup')
# v1_router.register(r'auth/token', RegistrationView, basename='token')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
