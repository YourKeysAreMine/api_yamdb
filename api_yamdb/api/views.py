from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from reviews.models import Title, Review
from api.serializers import CommentSerializer, ReviewSerializer, TitlePOSTSerializer, TitleGETSerializer
from api.permissions import (IsAdmin,
                             IsModerator,
                             IsAuthor,
                             ReadOnly,
                             IsAuthenticatedAndPOSTrequest)

from api.filters import TitleFilter


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


