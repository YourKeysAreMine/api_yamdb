from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(
        required=True,
        max_length=150,
        regex=r"^[^\W\d]\w*$",
    )

    class Meta:
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role'
        )
        model = User
        read_only_field = ('role',)
