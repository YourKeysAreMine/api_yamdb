from django.urls import include, path
from api.views import (GenreViewSet, 
                       CategoryViewSet, 
                       RegistrationView, 
                       ReviewViewSet, 
                       CommentViewSet, 
                       TitleViewSet)
from rest_framework.routers import DefaultRouter


router_v1 = DefaultRouter()

router_v1.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentViewSet,
    basename='comments',
)
router_v1.register(r'titles', TitleViewSet, basename='titles')
v1_router.register(r'genres', GenreViewSet, basename='genres')
v1_router.register(r'categories', CategoryViewSet, basename='categories')
v1_router.register(r'auth/signup', RegistrationView, basename='signup')
# v1_router.register(r'auth/token', RegistrationView, basename='token')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
