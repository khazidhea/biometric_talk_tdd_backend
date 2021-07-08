from faker import Faker
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient


def test_csrf_ok(api_client: APIClient):
    response: Response = api_client.get('/api/auth/csrf/')
    assert response.status_code == status.HTTP_200_OK
    assert 'csrftoken' in response.cookies


def test_register_ok(api_client: APIClient, db, fake):
    api_client = APIClient()

    username = fake.user_name()
    password = fake.password()
    print(username)
    print(password)
    response: Response = api_client.post(
        '/api/auth/register/',
        {
            'username': 'username',
            'password': 'password',
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
