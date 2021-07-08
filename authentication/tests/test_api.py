from hypothesis import given
from hypothesis import strategies as st
from hypothesis.extra.django import TestCase
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

from authentication.serializers import PASSWORD_REGEX, USERNAME_REGEX


def test_csrf_ok(api_client: APIClient):
    response: Response = api_client.get('/api/auth/csrf/')
    assert response.status_code == status.HTTP_200_OK
    assert 'csrftoken' in response.cookies


class TestAuth(TestCase):
    """Test creating users using hypothesis.

    Have to use TestCase over function with db fixture due to this bug:
    https://github.com/HypothesisWorks/hypothesis/issues/377
    The usernames generated are not unique and are not cleaned up resulting in errors
    """

    @given(
        username=st.from_regex(USERNAME_REGEX),
        password=st.from_regex(PASSWORD_REGEX),
    )
    def test_register_ok(self, username, password):
        print(username, password)
        api_client = APIClient()
        response: Response = api_client.post(
            '/api/auth/register/',
            {
                'username': username,
                'password': password,
            },
        )
        assert response.status_code == status.HTTP_201_CREATED


def test_register_already_exists(db, mixer, api_client: APIClient):
    user = mixer.blend('authentication.User')
    response: Response = api_client.post(
        '/api/auth/register/',
        {
            'username': user.username,
            'password': 'password123',
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'This field must be unique' in str(response.data['username'])


def test_register_short_password(db, api_client: APIClient, fake):
    response: Response = api_client.post(
        '/api/auth/register/',
        {
            'username': fake.user_name(),
            'password': '123',
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'This value does not match the required pattern' in str(response.data['password'])
