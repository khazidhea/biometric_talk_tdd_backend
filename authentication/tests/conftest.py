import pytest
from faker import Faker
from mixer.backend.django import Mixer
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture(scope='session')
def fake():
    fake = Faker()
    return fake


@pytest.fixture(name='mixer', scope='session')
def mixer_fixture():
    return Mixer()
