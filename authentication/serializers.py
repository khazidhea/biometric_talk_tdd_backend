from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from authentication.models import User

# Alphanumeric and longer than 5
USERNAME_REGEX = r'^\w{5,}$'
# Anything (excluding non printable characters) and longer than 8
PASSWORD_REGEX = '^[^\x00-\x20\x7F-\xA0$]{8,}$' # noqa


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.RegexField(
        regex=USERNAME_REGEX,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.RegexField(regex=PASSWORD_REGEX, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
