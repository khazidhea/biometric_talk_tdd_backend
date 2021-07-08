from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Base django user, open to future extension."""
