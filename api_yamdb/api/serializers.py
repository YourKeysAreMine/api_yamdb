from reviews.models import Genre, Category, User
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('email', 'username')
        model = User
