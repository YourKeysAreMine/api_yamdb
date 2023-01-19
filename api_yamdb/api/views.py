from reviews.models import Genre, Category
from rest_framework import viewsets, filters
from .serializers import GenreSerializer, CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # Добавить пермишены, пагинацию
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Добавить пермишены, пагинацию
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
