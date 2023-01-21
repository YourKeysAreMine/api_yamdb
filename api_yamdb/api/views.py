from reviews.models import Genre, Category
from rest_framework import viewsets, filters, views
from .serializers import GenreSerializer, CategorySerializer
import random
import string
from django.core.mail import send_mail


class GenreViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # Добавить пермишены.
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Добавить пермишены.
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'


class RegistrationView(views.APIView):

    def send_confirmation_code(self, email, user):
        confirmation_code = ''.join(
            random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        send_mail(
            subject='Yamdb! Код регистрации для получения JWT-токена',
            message=f''
        )

    def post(self, request):
        pass
