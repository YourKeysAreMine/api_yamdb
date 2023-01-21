from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, views

from reviews.models import Title, Review, Genre, Category
from api.serializers import (CommentSerializer, 
                             ReviewSerializer, 
                             TitlePOSTSerializer, 
                             TitleGETSerializer, 
                             GenreSerializer, 
                             CategorySerializer)
from api.permissions import (IsAdmin,
                             IsModerator,
                             IsAuthor,
                             ReadOnly,
                             IsAuthenticatedAndPOSTrequest)

from api.filters import TitleFilter
import random
import string
from django.core.mail import send_mail


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAdmin |
        IsModerator |
        IsAuthor |
        ReadOnly |
        IsAuthenticatedAndPOSTrequest,
    )

    def get_review(self, key):
        review_id = self.kwargs.get(key)
        review = get_object_or_404(Review, id=review_id)
        return review

    def get_queryset(self):
        review = self.get_review('review_id')
        new_queryset = review.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        review = self.get_review('review_id')
        serializer.save(author=self.request.user, review=review)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAdmin |
        IsModerator |
        IsAuthor |
        ReadOnly |
        IsAuthenticatedAndPOSTrequest,
    )

    def get_title(self, key):
        title_id = self.kwargs.get(key)
        title = get_object_or_404(Title, id=title_id)
        return title

    def get_queryset(self):
        title = self.get_title('title_id')
        new_queryset = title.reviews.all()
        return new_queryset

    def perform_create(self, serializer):
        title = self.get_title('title_id')
        serializer.save(author=self.request.user, title=title)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = (IsAdmin | ReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH', 'DEL'):
            return TitlePOSTSerializer
        return TitleGETSerializer


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
