import pytest
from faker import Faker
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture(scope='session')
def fake():
    fake = Faker()
    return fake
