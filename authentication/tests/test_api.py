from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient


def test_csrf_ok(api_client: APIClient):
    response: Response = api_client.get('/api/auth/csrf/')
    assert response.status_code == status.HTTP_200_OK
    assert 'csrftoken' in response.cookies
