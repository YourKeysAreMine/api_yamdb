from django.core.exceptions import ValidationError
from rest_framework import serializers
# from users.models import User


def validate_name(value):
    me = 'me'
    if value == me:
        raise serializers.ValidationError(
            f'Использовать имя {value} в качестве имя пользователя запрещено!'
        )


# def validate_unique_mail(value):
    # if User.objects.filter(email=value).exists():
        # raise ValidationError('Email, который Вы ввели - уже существует!')
    # return value
