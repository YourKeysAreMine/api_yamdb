from rest_framework import serializers
# from django.core.exceptions import ValidationError
# from rest_framework.response import Response
# from rest_framework import status
from .models import User
# from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):

    # def validate(self, value):
        # if User.objects.filter(username=value).exists() or User.objects.filter(email=value).exists():
            # return Response(status=status.HTTP_400_BAD_REQUEST)
        # return value

    username = serializers.RegexField(
        required=True,
        max_length=150,
        regex=r"^[^\W\d]\w*$",
        # validatiors=[
            # UniqueValidator(queryset=User.objects.all())
        # ]
    )

    class Meta:
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role'
        )
        model = User
        read_only_field = ('role',)
